import { ModeOfNotification } from "src/app/modules/models";

export function displayModeOfNotification(mode: ModeOfNotification): string {
    return mode && mode.label ? mode.label : '';
}