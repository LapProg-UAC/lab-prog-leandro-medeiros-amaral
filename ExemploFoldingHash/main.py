def foldingHash(hash_len, text, secret_key=None):
    """Divide text into columns of length hash_len and compute hash and signature.
    
    Args:
        hash_len: Length of each column
        text: Text to hash
        secret_key: Optional secret key to create signature
    
    Returns:
        blocks: List of blocks
        hashed_hex: Hash values in hex
        signature_hex: Signature values (hash + key) % 256 in hex if key provided
    """
    codes = [ord(c) for c in text]

    # Divide into blocks of hash_len
    blocks = []
    for i in range(0, len(codes), hash_len):
        block = codes[i : i + hash_len]
        if len(block) < hash_len:
            pad_value = int(hex(hash_len), 16)
            block.extend([pad_value] * (hash_len - len(block)))
        blocks.append(block)

    # Hash each column
    hashed = []
    for j in range(len(blocks[0])):
        column_sum = sum(block[j] for block in blocks) % 256
        hashed.append(column_sum)

    # Generate signature if secret key provided
    signature = None
    if secret_key:
        key_codes = [ord(c) for c in secret_key]
        # Pad or truncate key to match hash_len
        if len(key_codes) < hash_len:
            key_codes.extend([int(hex(hash_len), 16)] * (hash_len - len(key_codes)))
        else:
            key_codes = key_codes[:hash_len]
        
        # Signature: (hash + key) % 256
        signature = [(h + k) % 256 for h, k in zip(hashed, key_codes)]

    # Convert hash to hex
    hashed_hex = [hex(x)[2:].upper().zfill(2) for x in hashed]
    
    # Convert signature to hex if it exists
    signature_hex = None
    if signature:
        signature_hex = [hex(x)[2:].upper().zfill(2) for x in signature]

    return blocks, hashed_hex, signature_hex


if __name__ == "__main__":
    # Without secret key
    blocks, hash_result, _ = foldingHash(3, "Hello World")
    print("Hash:")
    print("  Blocks:", blocks)
    print("  Hash:", hash_result)
    
    # With secret key
    blocks, hash_result, signature = foldingHash(3, "Hello World", secret_key="KEY")
    print("\nWith secret key 'KEY':")
    print("  Blocks:", blocks)
    print("  Hash:", hash_result)
    print("  Signature:", signature)

##Leandro Medeiros Amaral 
##Francisco Rego Pinto