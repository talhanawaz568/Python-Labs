import argparse
parser = argparse.ArgumentParser(description='A simple greeting application.')

parser.add_argument('--name', type=str, help='The name of the person to greet.')
args = parser.parse_args()

if args.name:
	print(f"Hello, {args.name}!")
else:
	print("Hello, Stranger!")
