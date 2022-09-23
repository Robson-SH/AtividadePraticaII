from sitechecker.cli import read_user_cli_args

def main():
    user_args = read_user_cli_args()
    print (user_args)

if __name__ == "__main__":
    main()