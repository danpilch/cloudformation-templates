from lib.ec2.stack import Stack

def main():
    print(Stack().template.to_json())


if __name__ == "__main__":
    main()
