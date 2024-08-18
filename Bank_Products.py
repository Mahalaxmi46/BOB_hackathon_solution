# Correcting the CSV data
import pandas as pd

# Data in correct format
data = {
    "Product/Plan": [
        "Mutual Funds", "Alternate Investment Products", "Baroda 3 in 1 Demat & Trading Account",
        "Demat Account", "Atal Pension Yojana", "E-Kisan Vikas Patra Scheme", "Floating Rate Savings Bonds",
        "Gold Monetization Scheme", "Senior Citizen Savings Scheme", "Sovereign Gold Bonds", "Public Provident Fund (PPF)",
        "Sukanya Samriddhi Yojana", "National Pension Scheme (NPS)", "Mahila Samman Savings Certificate (MSSC) 2023",
        "Arogya Sanjeevani Policy", "National Mediclaim Plus Policy", "Burglary Insurance",
        "House Holders Insurance Policy", "Personal Accident Insurance", "National Parivar Mediclaim Plus Policy",
        "Shopkeepers Insurance", "Two Wheeler Insurance", "Chola MS Group Health Insurance", "Tata AIG Medicare",
        "National Mediclaim Policy", "National Super Top-Up Policy", "Auto Secure Private Car Package Policy",
        "Auto Secure Two-Wheeler Package Policy", "Travel Guard by TATA AIG", "Overseas Mediclaim Business and Holiday",
        "Overseas Mediclaim Employment and Studies", "Bharat Sookshma Udyam Suraksha Policy"
    ],
    "Description": [
        "Investment in a diversified portfolio of assets.", "Professionally managed investment strategies.",
        "Integrated bank, Demat, and trading account.", "Holds securities in electronic form.",
        "Retirement scheme providing a steady income post-60.", "Long-term savings instrument with assured returns.",
        "Government bonds with variable interest rates.", "Mobilizes gold from households for productive use.",
        "Savings scheme designed for seniors with high returns.", "Government security denominated in gold grams.",
        "Low-risk, long-term savings instrument with guaranteed returns.", "Savings scheme for the education and marriage of a girl child.",
        "Voluntary retirement savings scheme with systematic contributions.", "Savings scheme exclusively for women and girls.",
        "Standard health insurance with coverage up to 5 Lakhs.", "High sum insured policy covering in-patient treatment and day-care procedures.",
        "Covers movable property like stock, machinery against burglary.", "Comprehensive policy covering various home-related contingencies.",
        "Provides coverage for death, disablement, and weekly benefits.", "Floater policy covering all family members for in-patient treatment and day-care procedures.",
        "Omnibus policy designed for small shopkeepers.", "Insurance for two-wheelers covering accidental damage, theft, and natural calamities.",
        "Affordable group health plan covering up to 7 family members.", "Health insurance with cumulative bonus and restoration benefits.",
        "Covers in-patient treatment expenses and day-care procedures.", "Covers commonly excluded diseases with a one-year waiting period for pre-existing conditions.",
        "Insurance for cars against accidents, theft, and natural calamities.", "Insurance for two-wheelers against accidental damage, theft, and third-party property.",
        "Covers trip curtailment, hijacking, flight delay, and loss of checked-in baggage.", "Health insurance for international travel including medical expenses and personal accident.",
        "Insurance for overseas employment and studies covering medical expenses and personal accidents.", "Covers physical loss or damage to insured property due to fire, explosion, lightning, etc."
    ],
    "Key Features": [
        "Equity, Debt, and Gold options. Tax-efficient returns.", "Portfolio management services, structured products.",
        "Seamless and safe trading experience with a paperless account opening process.", "Facilitates easy storage and transactions.",
        "PRAN issued, aims to provide pension after age 60.", "Low-risk with a 7.5% interest rate.", "Interest rate reset half-yearly, no maximum investment limit.",
        "Interest rate based on deposit type, reduces reliance on gold imports.", "Allows multiple accounts with a combined maximum limit of Rs. 30 lakhs.",
        "2.5% interest paid half-yearly, substitute for physical gold.", "7.1% interest rate, tax rebate under Section 80C.",
        "8.2% interest rate, minimum annual deposit of Rs. 250 up to Rs. 1,50,000.", "Unique PRAN, flexible contribution options.",
        "7.5% interest rate, valid for two years up to March 31, 2025.", "Individual and floater options available.",
        "Cashless/Reimbursement basis with many additional benefits.", "Coverage for items that are reasonably protected.",
        "Bundled policy with ten sections, available for homeowners, tenants, housing societies, etc.", "Worldwide cover available 24X7.",
        "Unique features addressing health concerns with reasonable and customary expenses covered.", "Tailored to cover requirements of small shopkeepers.",
        "Comprehensive and liability-only options available.", "In-patient hospitalization covered up to Rs. 3,00,000.",
        "50% cumulative bonus, no medicals required.", "Minimum 24-hour hospitalization and coverage for 140+ procedures.",
        "Medical expenses reimbursed without sub-limits.", "Coverage up to Rs. 15,00,000.", "Liability only and comprehensive package options available.",
        "Provides coverage for various travel-related concerns.", "Provides comprehensive coverage for international trips.",
        "First USD 100 of all claims borne by the traveler.", "Comprehensive coverage including various risks."
    ],
    "Official Link": [
        "https://www.bankofbaroda.in/mutual-fund-investment", "https://www.bankofbaroda.in/alternate-investment",
        "https://www.bankofbaroda.in/baroda-3-in-1-account", "https://www.bankofbaroda.in/demat-account",
        "https://www.bankofbaroda.in/atal-pension-yojana", "https://www.bankofbaroda.in/e-kisan-vikas-patra",
        "https://www.bankofbaroda.in/floating-rate-savings-bonds", "https://www.bankofbaroda.in/gold-monetization-scheme",
        "https://www.bankofbaroda.in/senior-citizen-savings-scheme", "https://www.bankofbaroda.in/sovereign-gold-bonds",
        "https://www.bankofbaroda.in/public-provident-fund", "https://www.bankofbaroda.in/sukanya-samriddhi-yojana",
        "https://www.bankofbaroda.in/national-pension-scheme", "https://www.bankofbaroda.in/mahila-samman-savings-certificate",
        "https://www.bankofbaroda.in/arogya-sanjeevani-policy", "https://www.bankofbaroda.in/national-mediclaim-plus-policy",
        "https://www.bankofbaroda.in/burglary-insurance", "https://www.bankofbaroda.in/house-holders-insurance-policy",
        "https://www.bankofbaroda.in/personal-accident-insurance", "https://www.bankofbaroda.in/national-parivar-mediclaim-plus-policy",
        "https://www.bankofbaroda.in/shopkeepers-insurance", "https://www.bankofbaroda.in/two-wheeler-insurance",
        "https://www.bankofbaroda.in/chola-ms-group-health-insurance", "https://www.bankofbaroda.in/tata-aig-medicare",
        "https://www.bankofbaroda.in/national-mediclaim-policy", "https://www.bankofbaroda.in/national-super-top-up-policy",
        "https://www.bankofbaroda.in/auto-secure-private-car-package-policy", "https://www.bankofbaroda.in/auto-secure-two-wheeler-package-policy",
        "https://www.bankofbaroda.in/travel-guard-by-tata-aig", "https://www.bankofbaroda.in/overseas-mediclaim-business-and-holiday",
        "https://www.bankofbaroda.in/overseas-mediclaim-employment-and-studies", "https://www.bankofbaroda.in/bharat-sookshma-udyam-suraksha-policy"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_file = "/mnt/data/bank_products_corrected.csv"
df.to_csv(output_file, index=False)

output_file
