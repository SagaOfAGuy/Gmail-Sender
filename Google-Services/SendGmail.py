from Gmail import send_text
import argparse
if __name__ == "__main__":
    example = ''' examples:
    
    python3 SendGmail.py -to recipient@gmail.com -subject "Test" -message "This is a test"
    
    python3 SendGmail.py -to recipient@gmail.com -subject "Test #2" -message "Testing testing!"

    '''
    my_parser = argparse.ArgumentParser(description='Send Gmail Email via Command-Line', epilog=example,formatter_class=argparse.RawDescriptionHelpFormatter)
    my_parser.add_argument("-to", type=str, default=1.0, help="")
    my_parser.add_argument("-subject", type=str, default=1.0, help="")
    my_parser.add_argument("-message", type=str, default=1.0, help="")
    args = my_parser.parse_args()
    send_text(args.to, args.subject, args.message)