from server.files import LogFile, clear_logs


def test_clear_logs_truncates_file(tmp_path) -> None:
    log_path = tmp_path / "data.log"
    with LogFile(str(log_path), mode="w") as lg:
        lg.write("hello\n")

    clear_logs(str(log_path))

    with LogFile(str(log_path), mode="r") as lg:
        assert lg.read() == ""

