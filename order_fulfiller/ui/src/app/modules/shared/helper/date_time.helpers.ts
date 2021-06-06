export function formatDate(date: any): string {
    const _date = new Date(date);
    const day = _date.getDate();
    const month = _date.getMonth() + 1;
    const year = _date.getFullYear();
    return `${month}/${day}/${year}`;
}

export function formatDateYYYYMMDDD(date: any): string {
    const _date = new Date(date);
    const day = _date.getDate();
    const month = _date.getMonth() + 1;
    const year = _date.getFullYear();
    return `${year}-${month}-${day}`;
}

export function formatTime(date: Date): string {
    const _date = new Date(date);
    const hours = _date.getHours()
    const minutes = _date.getMinutes();
    const seconds = _date.getSeconds();
    return `${hours}:${minutes}:${seconds}`;
}
export function toDateTimestamp(date: Date): string {
    const dateStamp = formatDate(date);
    const timeStamp = formatTime(date);
    return `${dateStamp} ${timeStamp}`
}
export function calculateDays(fromDate: any, toDate: any): number {
    const FromDate = new Date(fromDate);
    const ToDate = new Date(toDate);
    const difference = ToDate.getTime() - FromDate.getTime();
    const days = Math.round((difference / (1000 * 60 * 60 * 24)));
    return days;
}

export function calculateTime(fromDate: any, toDate: any): string {
    const FromDate = new Date(fromDate);
    const ToDate = new Date(toDate);
    const difference = ToDate.getTime() - FromDate.getTime();
    return formatTime(new Date(difference))
}

export function formatAMPM(date: Date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    var minutesStr = minutes < 10 ? '0' + minutes : minutes;
    var strTime = hours + ':' + minutesStr + ' ' + ampm;
    return strTime;
}