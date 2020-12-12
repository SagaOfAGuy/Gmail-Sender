import argparse
from Gmail import send_attachment, get_messages, delete_messages_bulk
import sys 
if __name__ == "__main__":
    example = ''' examples:
    
    python3 SendGmailAttachment.py -to recipient@gmail.com -subject "Test Image" -attachment "path/to/image"
    
    python3 SendGmailAttachment.py -to recipient@gmail.com -subject "Test Image #2" -attachment "/path/to/image1.png" "/path/to/image2.png" "/path/to/image3.png"

    '''
    my_parser = argparse.ArgumentParser(description='Send Gmail Email via Command-Line', epilog=example,formatter_class=argparse.RawDescriptionHelpFormatter)
    my_parser.add_argument("-to", type=str, default=1.0, help="")
    my_parser.add_argument("-subject", type=str, default=1.0, help="")
    my_parser.add_argument("-attachment", type=str, default=1.0, help="", nargs="+")
    args = my_parser.parse_args()
    attachment_flags = args.attachment
    send_attachment(args.to, args.subject,attachment_flags)


    