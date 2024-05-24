def barcode_reader(barcode):
    return None


if __name__ == '__main__':
    assert barcode_reader(
        '_ _   _ __ _  ___ __  __  _  __ ____ _  ___ _ _ _ __  __ __ __  _    _ _ ___  _  ___ _   _  _ _'
    ) == '5901234123457', '5901234123457'

    assert barcode_reader(
        '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    ) == '4299687613665', '4299687613665'

    assert barcode_reader(
        '_ _ ___ __  __  _  _  __ ____ _ _   __ __   _ _ _ _ _    _   _  _  _   ___ _  __  __ __ __  _ _'
    ) is None, '0712345678912 : wrong check digit (right: 1)'

    assert barcode_reader(
        '___  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    ) is None, 'wrong left guard bar'

    assert barcode_reader(
        '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ ___ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    ) is None, 'wrong center bar'

    assert barcode_reader(
        '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ ___'
    ) == None, 'wrong right guard bar'

    print("Check done.")
