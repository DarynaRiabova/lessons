import random

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Session, relationship

DATABASE_URL = "postgresql+psycopg2://darynariabova@localhost/students_db"

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


student_courses = Table(
    "student_courses",
    Base.metadata,
    Column(
        "student_id",
        ForeignKey("students.id"),
        primary_key=True,
    ),
    Column(
        "course_id",
        ForeignKey("courses.id"),
        primary_key=True,
    ),
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    courses = relationship(
        "Course",
        secondary=student_courses,
        back_populates="students",
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)

    students = relationship(
        "Student",
        secondary=student_courses,
        back_populates="courses",
    )


Base.metadata.create_all(engine)
with Session(engine) as session:
    course_titles = ["Python", "SQL", "Java", "C++", "JavaScript"]

    for title in course_titles:
        course = session.query(Course).filter_by(title=title).first()

        if course is None:
            session.add(Course(title=title))

    session.commit()

    courses = session.query(Course).all()

    for i in range(1, 21):
        email = f"student{i}@gmail.com"

        student_exists = session.query(Student).filter_by(email=email).first()

        if student_exists:
            continue

        student = Student(
            name=f"Student {i}",
            email=email,
        )
        student.courses = random.sample(
            courses,
            k=random.randint(1, 3),
        )

        session.add(student)

    session.commit()
