from emaildump import EmailDump


def main():
    dump = EmailDump();
    dump.parse_csm_file()
    dump.parse_users_file()
    dump.filter_scpd_users()
    dump.filter_mooc_users()
    dump.generate_scpd_and_mooc_users()
    dump.dump_users()
    dump.parse_completed_file()
    dump.dump_completed()

if __name__ == "__main__":
    main()
