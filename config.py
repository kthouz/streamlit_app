ENV = "local" # it take values local, dev, prod
FORCE_TRAINING = True
TRAINING_FREQUENCY = 7
RANDOM_SEED = 4723
MIN_LOCATION_SAMPLES = 100
BRANCHES = ["RULINDO"]
LOCATIONS = [
    "AMAJYARUGURU_RULINDO_MURAMBI",
    "AMAJYARUGURU_RULINDO_MASORO",
    "AMAJYARUGURU_RULINDO_BUSHOKI",
    "AMAJYARUGURU_RULINDO_MBOGO",
    "AMAJYARUGURU_RULINDO_BASE",
    "AMAJYARUGURU_RULINDO_BUYOGA",
    "AMAJYARUGURU_RULINDO_KINIHIRA",
    "AMAJYARUGURU_RULINDO_CYUNGO",
    "AMAJYARUGURU_RULINDO_TUMBA",
    "AMAJYARUGURU_RULINDO_RUKOZO",
    "AMAJYARUGURU_RULINDO_KISARO",
    "AMAJYARUGURU_RULINDO_SHYORONGI",
    "AMAJYARUGURU_RULINDO_RUSIGA",
    "AMAJYARUGURU_RULINDO_BUREGA",
    "AMAJYARUGURU_RULINDO_CYINZUZI",
    "AMAJYARUGURU_RULINDO_NGOMA",
    "AMAJYARUGURU_RULINDO_NTARABANA"
]
BATCH_SIZE = 4

TIMEZONE = "Africa/Kigali"
if ENV=="local":
    PATH_TO_JOBS = "jobs"
    PATH_TO_LOGS = "logs"
    PATH_TO_CREDENTIALS = "credentials.json"
else:
    PATH_TO_JOBS = "/opt/airflow/jobs"
    PATH_TO_LOGS = "/opt/airflow/logs"
    PATH_TO_CREDENTIALS = "/opt/airflow/dags/credentials.json"
PANDAS_TOSQL_IF_EXISTS = "append"

ROLLING_STATS_WINDOW = 12
VENDING_CATEGORIES = ["broadcasters", "health facilities", "hotels", "medium industries", "non residential", "residential", "small industries", "telecom towers", "wtp and wps"]

CATALOG = {
    "branch": "branch", 
    "vending_category": "category",
    "lifetime": "lifetime",
    "lifetime_total_units": "lifetime purchased units",
    "lifetime_total_transactions": "lifetime total transactions",
    "total_blank_periods": "total count of blank periods",
    "longest_blank_period_length": "longest blank period",
    "last_blank_period_length": "last blank period",
    "months_since_last_blank_period": "months since last blank period",
    "months_since_longest_blank_period": "months since longest blank period",
    "avg_monthly_units_over_blank_periods": "average monthly units over blank periods",
    "std_monthly_units_over_blank_periods": "standard deviation monthly units over blank periods",
    "monthly_units_over_last_blank_period": "estimated monthly units over the last blank period",
    "monthly_units_over_longest_blank_period": "estimated monthly units over the longest blank period",
    "units_avg_3": "last three months average units",
    "units_avg_6": "last six months average units",
    "units_avg_12": "last twelve months average units",
    "rel_units_avg_3_6": "relative gap between last three and last six months average units",
    "rel_units_avg_3_12": "relative gap between last three and last twelve months average units",
    "rel_units_avg_6_12": "relative gap between last six and last twelve months average units",
    "rel_units_avg_3_6_df": "rate of change of the relative gap between last three and last six months average units",
    "rel_units_avg_3_12_df": "rate of change of the relative gap between last three and last twelve months average units",
    "rel_units_avg_6_12_df": "rate of change of the relative gap between last six and last twelve months average units",
    "rel_units_avg_3_6_ddf": "curvature of the relative gap between last three and last six months average units",
    "rel_units_avg_3_12_ddf": "curvature of the relative gap between last three and last twelve months average units",
    "rel_units_avg_6_12_ddf": "curvature of the relative gap between last six and last twelve months average units",
    "units_avg_3_rank": "categorical percentile of the last three average units",
    "units_avg_6_rank": "categorical percentile of the last six average units",
    "units_avg_12_rank": "categorical percentile of the last twelve average units",
    "urb_pct": "location urbanization level",
    "total_units_before_last_blank_period": "units before the last blank period", 
    "total_units_before_longet_blank_period": "units before the longest blank period", 
    "estimated_last_blank_period_monthly_units": "estimated last blank period monthly units",
    "location": "location",
    "is_violation": "is fraud",
}
CATALOG = dict(sorted(CATALOG.items(), key=lambda x: len(x[0]), reverse=True))

RULES_CUTOFFS = {
    "class_one_negative": {
        "rel_units_avg_3_6__absmax": 0.25,
        "rel_units_avg_3_6_df__min": -0.2,
        "rel_units_avg_3_6_ddf__min": -0.2,
        "last_blank_period_length__max": 0,
        "months_since_last_blank_period__min": 12,
        "units_avg_3_rank__min": 0.3,
        "units_avg_3_rank__max": 0.7,
        "vending_category__include": ["healthfacilities", "mediumindustries", "broadcasters", "wtpandwps", "telecomtowers"]
        
        },
    "class_two_negative": {
        "vending_category__include": ["telecomtowers"],
        "last_blank_period_length__max": 0,
        "months_since_last_blank_period__min": 24,
    },
    "class_one_positive": {
        "last_blank_period_length__max": 12,
        "last_blank_period_length__min": 6,
        "rel_units_avg_3_6__max": -0.9,
        "rel_units_avg_3_6_df__max": -0.5,
        "rel_units_avg_3_6_ddf__max": -0.5,
        "months_since_longest_blank_period__max": 12,
        "units_avg_3_rank__max": 0.1,
        "rel_units_avg_3_6__max": -0.25,
        "cv_monthly_units_over_blank_periods__min": 0.25,
    }
}

PROB_CUTOFF = 0.95
IDENTIFIERS = ["poc_number", "meter_number"]
RULES_TARGET = "is_violation"
RULES_PREDICTORS = [
    "lifetime",
    "total_blank_periods",
    "longest_blank_period_length",
    "last_blank_period_length",
    "idle",
    "lifetime_monthly_units",
    "months_since_longest_blank_period",
    "months_since_last_blank_period",
    "rel_units_avg_3_6",
    "rel_units_avg_3_6_df",
    "rel_units_avg_3_12",
    "rel_units_avg_3_12_df",
    "rel_units_avg_6_12",
    "rel_units_avg_6_12_df",
    "rel_units_avg_3_lifetime",
    "rel_units_avg_6_lifetime",
    "rel_units_avg_12_lifetime",
    "avg_monthly_units_over_blank_periods",
    "cv_monthly_units_over_blank_periods",
    "total_units_before_last_blank_period", 
    "total_units_before_longest_blank_period", 
]

assert len(RULES_PREDICTORS)==len(set(RULES_PREDICTORS))

REGR_PREDICTORS = [
    'longest_blank_period_length',
    'last_blank_period_length', 
    'months_since_longest_blank_period',
    'months_since_last_blank_period', 
    'lifetime_monthly_units',
    'units_avg_3',
    'most_freq_week',
    'units', 
    'units_dev_from_normal_avg_3',
    'units_dev_from_normal_lifetime', 
    # 'daily_units_12', 'daily_units_11',
    # 'daily_units_10', 'daily_units_9', 'daily_units_8', 'daily_units_7',
    # 'daily_units_6', 'daily_units_5', 'daily_units_4', 'daily_units_3',
    # 'daily_units_2',
    'avg_daily_units', 'std_daily_units', 'min_daily_units', 'max_daily_units', 
    'mid_daily_units', 'q25_daily_units', 'q50_daily_units', 'q75_daily_units',
    'vending_category_is_healthfacilities',
    'vending_category_is_nonresidential', 
    'vending_category_is_residential',
    'vending_category_is_smallindustries'
]

LAST_N_TRANSACTIONS = 24
REGR_SEQ_LEN = 12
REGR_TARGET_RANK = 1
REGR_TARGET = "dtnt_1"
REGR_NUMERICAL_COLS = ["dtnt", "units", "daily_units"]


