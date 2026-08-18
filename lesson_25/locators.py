# XPATH
XPATH_LOGO = "//a[@class='header_logo']"
XPATH_TEXT_HOME = "//a[text()='Home']"
XPATH_ABOUT = "//button[text()='About']"
XPATH_CONTACTS = "//button[text()='Contacts']"
XPATH_GUEST_LOG_IN = "//button[text()='Guest log in']"
XPATH_SIGN_IN = "//button[text()='Sign In']"
XPATH_ATTRIBUTE = "//a[@href='/']"
XPATH_ABOUT_SECTION = "//button[@appscrollto='aboutSection']"
XPATH_CONTACTS_SECTION = "//button[@appscrollto='contactsSection']"
XPATH_GUEST = "//button[contains(@class, '-guest')]"
XPATH_SIGN_IN_BY_CLASS = "//button[contains(@class, 'header_signin')]"
XPATH_HOME_NAV = "//nav//a[text()='Home']"
XPATH_ABOUT_NAV = "//nav//button[text()='About']"
XPATH_CONTACTS_NAV = "//nav//button[text()='Contacts']"
XPATH_SIGN_IN_INSIDE_BLOCK = (
    "//div[contains(@class, 'header_right')]//button[text()='Sign In']"
)
XPATH_DO_MORE = "//h1[text()='Do more!']"
XPATH_DESCRIPTION = "//p[contains(text(), 'Hillel auto project')]"
XPATH_SIGN_UP = "//button[text()='Sign up']"
XPATH_SIGN_UP_INSIDE_DESCRIPTION = (
    "//div[@class='hero-descriptor']//button[text()='Sign up']"
)
XPATH_DO_MORE_HERO = "//section[contains(@class, 'hero')]//h1[text()='Do more!']"
XPATH_SIGN_UP_INSIDE_HERO_CLASS = (
    "//section[contains(@class, 'hero')]//button[text()='Sign up']"
)
XPATH_YOUTUBE = "//iframe[contains(@src, 'youtube.com/embed')]"
XPATH_YOUTUBE_BY_CLASS = "//iframe[@class='hero-video_frame']"
XPATH_IMG = "//img[@alt='Instructions']"
XPATH_IMG_INSIDE_ABOUT_PICTURE = (
    "//div[contains(@class, 'about-picture')]//img[@alt='Instructions']"
)

#  CSS LOCATORS

# 1. Logo
CSS_01 = "a.header_logo"
# 2. Home
CSS_02 = "a.btn.header-link.-active"
# 3. About
CSS_03 = "button[appscrollto='aboutSection']"
# 4. Contacts
CSS_04 = "button[appscrollto='contactsSection']"
# 5. Guest log in
CSS_05 = "button.header-link.-guest"
# 6. Sign In
CSS_06 = "button.header_signin"
# 7. Home by href
CSS_07 = "nav a[href='/']"
# 8. About inside nav
CSS_08 = "nav button[appscrollto='aboutSection']"
# 9. Contacts inside nav
CSS_09 = "nav button[appscrollto='contactsSection']"
# 10. Guest button inside header
CSS_10 = "header button.-guest"
# 11. Sign In inside header
CSS_11 = "header button.header_signin"
# 12. Logo inside header
CSS_12 = "header a.header_logo"
# 13. Home inside header navigation
CSS_13 = "header nav a.header-link"
# 14. About inside header navigation
CSS_14 = "header nav button[appscrollto='aboutSection']"
# 15. Sign In inside header right block
CSS_15 = "div.header_right button.header_signin"
# 16. Hero title
CSS_16 = "h1.hero-descriptor_title"
# 17. Hero description
CSS_17 = "p.hero-descriptor_descr"
# 18. Sign up
CSS_18 = "button.hero-descriptor_btn"
# 19. Sign up inside descriptor
CSS_19 = "div.hero-descriptor button.btn-primary"
# 20. Hero title inside section
CSS_20 = "section.hero h1.hero-descriptor_title"
# 21. Sign up inside hero section
CSS_21 = "section.hero button.hero-descriptor_btn"
# 22. YouTube iframe by src
CSS_22 = "iframe[src*='youtube.com/embed']"
# 23. YouTube iframe by class
CSS_23 = "iframe.hero-video_frame"
# 24. Instructions image by alt
CSS_24 = "img[alt='Instructions']"
# 25. Instructions image inside about picture
CSS_25 = "div.about-picture img.about-picture_img"
