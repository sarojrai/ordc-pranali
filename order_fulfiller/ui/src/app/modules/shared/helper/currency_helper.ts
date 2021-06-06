export function convertToDecimal(currency: number | string | null) {
    if (currency !== undefined && currency !== null) {
        var splitString = currency.toString().split(".");
        return splitString[1];
    }
    return "";
}