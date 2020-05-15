import Email_scraper.scraper as sc
import Email_scraper.GUI as gui


if __name__ == "__main__":
    try:
        login, password, place, per_of_time, file_format = gui.graphic_interface()
        sc.reading_emails(file_format, place, per_of_time, login, password)
    except TypeError:
        raise SystemExit
