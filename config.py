import os

BASE_DIR = os.path.dirname(__file__)

EXCEL_PATH = os.path.join(BASE_DIR, "data", "maharera_final_clean.xlsx")
GRAPHS_DIR = os.path.join(BASE_DIR, "data", "graphs")

PORT       = int(os.environ.get("PORT", 5000))
SECRET_KEY = os.environ.get("SECRET_KEY", "SERTyhu7654EDFGhbhY^%$5678ijHBVCDEr")

# ── Supabase ──────────────────────────────────────────────
SUPABASE_URL          = os.environ.get("SUPABASE_URL",          "https://gbojjpasnzevczvyndlx.supabase.co")
SUPABASE_ANON_KEY     = os.environ.get("SUPABASE_ANON_KEY",     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imdib2pqcGFzbnpldmN6dnluZGx4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM2NTM3MzEsImV4cCI6MjA4OTIyOTczMX0.CMtIA-pSaZqsVffjM9_DISenQMWh4u6pWXZB680TFys")
SUPABASE_SERVICE_KEY  = os.environ.get("SUPABASE_SERVICE_KEY",  "")  # Set this in Railway env vars
