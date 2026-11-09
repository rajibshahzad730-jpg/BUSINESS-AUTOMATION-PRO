# Business Automation Pro

A professional desktop application that turns raw **Excel / CSV sales data** into **clean datasets, PDF reports, numbered invoices and exports** – in a few clicks. It has a modern, glass-style interface with smooth animations, and a command-line mode for automation.

![Demo](docs/demo.gif)

## Features

| | |
|---|---|
| **Excel data processing** | Reads `.xlsx` / `.xlsm` / `.csv`. Recognises flexible headers (`Qty`, `Client Name`, `Price`…), fixes text numbers (`Rs 1,000`), mixed date formats, stray spaces and inconsistent letter case, removes duplicates and invalid rows, and logs every fix. |
| **PDF report generator** | Branded multi-page report: KPIs, revenue-by-month chart, top customers (chart + ranked table), top products, data-quality notes. |
| **Automatic invoice creation** | One invoice per customer (or per `Invoice No`), sequential numbering that survives restarts (`INV-2026-0001`), tax, due dates, your logo colour and company details. |
| **Data export** | Excel (formatted, filters, live `SUM` totals, summary sheets), CSV (UTF-8) and JSON. |
| **Professional desktop UI** | Frosted-glass cards on an aurora backdrop, sliding navigation pill, animated KPI counters and charts, ripple buttons, toast notifications, page transitions. Runs work in background threads so it never freezes. |
| **CLI mode** | `python main.py data.xlsx --all` for scheduled / headless use. |

## Screenshots

| Data overview | PDF report |
|---|---|
| ![Data](docs/screenshots/02-data.png) | ![Report](docs/screenshots/04-report-done.png) |
| **Invoices** | **Export** |
| ![Invoices](docs/screenshots/05-invoices.png) | ![Export](docs/screenshots/06-export.png) |

## Quick start

```bash
git clone <your-repo-url>
cd business-automation-pro
pip install -r requirements.txt
python main.py                 # opens the desktop app
```

Click **Load sample** to try everything instantly with realistic, deliberately messy demo data.

> Linux: Tkinter may need `sudo apt install python3-tk`.

### Command line

```bash
python main.py --sample --all                      # report + invoices + Excel export
python main.py sales.xlsx --report                 # only the PDF report
python main.py sales.xlsx --invoices --invoice-mode invoice_no
python main.py sales.csv --export json --out ./results
```

## Input format

Required columns (names are matched flexibly): **Date, Customer, Product, Quantity, Unit Price**.
Optional: **Email, Address, Invoice No**. See `sample_data/sample_sales.xlsx`.

## Project structure

```
main.py                  entry point (GUI or CLI)
app/
  config.py              settings (company, tax, currency…) persisted to settings.json
  data_processor.py      load / clean / validate / summarise
  report_generator.py    PDF sales report (ReportLab)
  invoice_generator.py   invoice model, numbering, PDF rendering
  exporter.py            Excel / CSV / JSON export
  controller.py          workflow orchestration shared by GUI and CLI
  cli.py                 command-line interface
  gui.py                 desktop application (pages, actions)
  ui/                    glass widget toolkit (Pillow-rendered canvases, tween engine, icons)
sample_data/             demo workbook
tests/                   pytest suite (data, invoices, reports, export, CLI, GUI smoke)
tools/                   screenshot + demo-GIF recorders
```

## Development

```bash
pip install -r requirements-dev.txt
python -m pytest -q                       # GUI tests are skipped without Tk/display
python -m app.sample_generator            # regenerate the sample workbook
xvfb-run -a python tools/gui_screenshots.py docs/screenshots   # refresh screenshots (Linux)
```

### Build a Windows `.exe`

Run `build_windows.bat` – it produces `dist/BusinessAutomationPro.exe` with PyInstaller.

## Customising

Open **Settings** in the app to set your company name, address, currency, tax rate, payment terms, invoice prefix, accent colour and output folder. These appear on every PDF.

## Roman Urdu mukhtasar

Yeh software Excel/CSV data ko saaf karta hai, PDF sales report banata hai, invoices khud-ba-khud generate karta hai aur data ko Excel/CSV/JSON mein export karta hai. `python main.py` chalayen aur **Load sample** dabayen.

## License

MIT – see [LICENSE](LICENSE).
