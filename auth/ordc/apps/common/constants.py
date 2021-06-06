class APIParameter:
    #  App name User, this constants will be used in user app api to retrieve the data
    MOBILE_NUMBER = "mobileNumber"
    CLIENT_ID = "clientId"
    OTP = "otp"
    PASSWORD = "password"
    CONFIRM_PASSWORD = "confirmPassword"
    USERNAME = "username"
    EMAIL = "email"
    PHONE = "phone"
    FIRST_NAME = "firstName"
    NAME = "name"
    DOB = "dob"
    AGE_GROUP = "ageGroup"
    DATE_OF_BIRTH = "dateOfBirth"
    GENDER = "gender"
    AVATAR = "avatar"
    USER_ID = "userId"
    CHILD_ID = "childId"
    WACONSENT = "waconsent"

    LAT = "lat"
    LONG = "long"
    AREA = "area"
    LANG = "lang"
    CATEGORY_ID = "categoryId"

    # App name coupon, this constants will be used in coupon app api to retrieve the data
    COUPON_CODE = "couponCode"
    AMOUNT = "amount"
    DISCOUNT = "discount"
    CASH_VOUCHER_CODE = "cashVoucherCode"
    SUBSCRIPTION_PACKAGE_ID = "subscriptionPackageId"
    REFERRAL_DISCOUNT_APPLIED = "referralRewardApplied"

    # App name Payment, this constants will be used in Payment app api to retrieve the data
    TXN_ID = "txnId"
    PRODUCT_INFO = "productInfo"
    KEY = "key"
    PAYMENT_ID = "paymentId"
    PAYU_PAYMENT_RESPONSE = "payUResponse"

    # App name Video, this constants will be used in Video app api to retrieve the data
    EPISODE_ID = "episodeId"
    SHOW_ID = "showId"
    TOPIC_ID = "topicId"

    # english app
    CHILD_ACTIVITY_ID = "childActivityId"
    ACTIVITY_ID = "activityId"
    LAST_ATTEMPTED_AT = "lastAttemptedAt"
    REFCODE = "refcode"
    LEARNING_LEVEL_ID = "learningLevelId"
    PRACTICE_ACTIVITY_ID = "englishPracticeActivityId"
    CHILD_MATH_QUESTION_ID = "childMathQuestionId"
    CHILD_VIDEO_ACTIVITY_ID = "childEnglishActivityId"

    # Maths specfic params here.

    CHAPTER_ID = "chapterId"
    COURSE_ID = "courseId"

    # App name Maths, this constants will be used in Maths app api to retrieve the data
    SKILL_ID = "skillId"


class DictKeyConstants:
    #  App name User, this constants will be used as dict key to reduce the typo error
    NICK_NAME = "nick_name"
    GENDER = "gender"
    FIRST_NAME = "first_name"
    AGE_GROUP = "age_group"
    AVATAR = "avatar"
    LOCAL_ID = "local_id"
    DOB = "dob"
    USER_ID = "user_id"
    CHILD_ID = "child_id"

    MOBILE_NO = "mobile_number"
    OTP = "otp"
    USERNAME = "username"
    CLIENT_ID = "client_id"
    PASSWORD = "password"
    CNF_PASSWORD = "confirm_password"
    WA_CONSENT = "wa_consent"

    #  App name coupon, this constants will be used as dict key to reduce the typo error
    VOUCHER_CODE = "voucher_code"

    # child activity
    ACTION = "action"
    CHILD_ACTIVITY_ID = "child_activity_id"
    ACTIVITY_ID = "activity_id"
    ATTEMPTED_AT = "attempted_at"
    PRACTICE_ACTIVITY_ID = "englishPracticeActivityId"

    VIEW_COUNT = "view_count"
    ATTEMPT_COUNT = "attempt_count"
    ATTEMPT = "attempt"

    # coupon
    COUPON_CODE = "coupon_code"
    SUBSCRIPTION_PACKAGE_ID = "subscription_package_id"


class RestConstant:
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"

class TenderConstant:

    TENDER_TYPE = (
        ("PUBLIC", "Public"),
        ("PRIVATE", "Private"),
    )
    TENDER_STATUS = ((0, "Deactive"), (1, "Active"))

    TRANSPORT_TYPE = (
        ("AVIATION", "Aviation"),
        ("MARINE", "Marine"),
        ("RAILWAYS", "Railways"),
        ("ROADWAYS", "Roadways"),
    )
    RATE_UNIT =(
        ("KG", "kg"),
        ("TON", "ton")
        
    )

    APPLICABLE_FOR = (
        (1, "Transportation"),
        (2, "Telecommunications"),
        (3, "Industry"),
        (4, "Agriculture, Food and Beverages"),
    )
    
    STATUS = (
        (0, "DRAFT"),
        (1, "ACTIVE"),
        (2, "DEACTIVE"),
        (111, "CANCEL"),
        (999, "CLOSE"),
    )