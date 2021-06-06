import { Component, Inject, ViewEncapsulation } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

export interface DialogData {
    message: string
}

@Component({
    selector: 'confirmation-dialog',
    templateUrl: './confirmation.dialog.component.html',
    styleUrls: ['./confirmation.dialog.component.scss'],
    encapsulation: ViewEncapsulation.None,
})
export class ConfirmationDialog {

    constructor(
        public dialogRef: MatDialogRef<ConfirmationDialog>,
        @Inject(MAT_DIALOG_DATA) public data: DialogData) { }

    onNoClick(): void {
        this.dialogRef.close();
    }
}