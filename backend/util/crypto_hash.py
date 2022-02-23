import hashlib
import json


def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    # takes all the arguments and concats into a string
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)

    # then take the string and encodes them
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash('one two three'): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash('one two three'): {crypto_hash(2, 'one', [3])}")


if __name__ == '__main__':
    main()
