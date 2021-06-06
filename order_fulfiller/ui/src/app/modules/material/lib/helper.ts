export function numberWithCommas(x: string) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}


export const ORDER_RANGE_FORMATS = {
    parse: {
        dateInput: "LL"
    },
    display: {
        dateInput: "DD MMM, YYYY",
        monthYearLabel: "MMM YYYY",
        dateA11yLabel: "LL",
        monthYearA11yLabel: "MMMM YYYY"
    }
};


export function compareDates(source: Date, to: Date) {
    return source < to;
}

export function convertRemainingDays(from: Date, to: Date) {
    let oneDay = 1000 * 60 * 60 * 24;
    let oneHour = 1000 * 60 * 60;
    let oneMinute = 1000 * 60;
    let diff = Math.abs(from.getTime() - to.getTime());
    let days, hours, minutes;
    days = hours = minutes = 0
    days = diff / oneDay;
    diff = diff - (days * oneDay);
    hours = diff / oneHour;
    diff = diff - (hours * oneHour);
    minutes = diff / oneMinute;
    return days.toLocaleString(undefined, { minimumIntegerDigits: 2, useGrouping:false, maximumFractionDigits: 0 })
        + "d " + hours.toLocaleString(undefined, { minimumIntegerDigits: 2, useGrouping:false, maximumFractionDigits: 0 })
        + "h " + minutes.toLocaleString(undefined, { minimumIntegerDigits: 2, useGrouping:false, maximumFractionDigits: 0 }) + "m";
}