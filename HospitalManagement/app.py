from tkinter import *
from tkinter import ttk
import function
import time
import random
import datetime
import tempfile
import tkinter.messagebox


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background='darkblue')



        cmbNameTablets = StringVar()
        ref = StringVar()
        dose = StringVar()
        numberTablets = StringVar()
        lot = StringVar()
        issueDate = StringVar()
        issueDate.set(time.strftime("%d/%m/%Y"))
        expDate = StringVar()
        dailyDose = StringVar()
        possibleSideEffects = StringVar()
        furtherInfomation = StringVar()
        storageAdvice = StringVar()
        drivingUsingMachine = StringVar()
        howtoUseMedication = StringVar()
        patientID = StringVar()
        patientNHSNO = StringVar()
        patientName = StringVar()
        dateOfBirth = StringVar()
        patientAddress = StringVar()
        prescription = StringVar()

        # ==================================functions ====================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Hospital management system", "confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def iDelete():
            cmbNameTablets.set("")
            ref.set("")
            dose.set("")
            numberTablets.set("")
            lot.set("")
            issueDate.set("")
            expDate.set("")
            dailyDose.set("")
            possibleSideEffects.set("")
            furtherInfomation.set("")
            storageAdvice.set("")
            drivingUsingMachine.set("")
            howtoUseMedication.set("")
            patientID.set("")
            patientNHSNO.set("")
            patientName.set("")
            dateOfBirth.set("")
            patientAddress.set("")
            self.txtPrescription.delete("1.0", END)
            self.texFrameDetail.delete("1.0", END)
            return

        def iReset():
            cmbNameTablets.set("")
            ref.set("")
            dose.set("")
            numberTablets.set("")
            lot.set("")
            issueDate.set("")
            expDate.set("")
            dailyDose.set("")
            possibleSideEffects.set("")
            furtherInfomation.set("")
            storageAdvice.set("")
            drivingUsingMachine.set("")
            howtoUseMedication.set("")
            patientID.set("")
            patientNHSNO.set("")
            patientName.set("")
            dateOfBirth.set("")
            patientAddress.set("")
            self.txtPrescription.delete("1.0", END)
            # self.texFrameDetail.delete("1.0", END)
            return

        def iPrescriptionData():
            self.texFrameDetail.insert(END, cmbNameTablets.get() + "\t\t" +
                                       ref.get() + "\t" +
                                       dose.get() + "\t\t" +
                                       numberTablets.get() + "\t" +
                                       lot.get() + "\t" +
                                       issueDate.get() + "\t\t" +
                                       expDate.get() + "\t" +
                                       dailyDose.get() + "\t\t" +
                                       storageAdvice.get() + "\t" +
                                       patientNHSNO.get() + "\t\t" +
                                       patientName.get() + "\t" +
                                       dateOfBirth.get() + "\t" +
                                       patientAddress.get() + "\n")
            return

        def iPrescription():
            self.txtPrescription.insert(END, 'Name of Tablet: \t\t\t' + cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END, 'Reference No: \t\t\t' + ref.get() + "\n")
            self.txtPrescription.insert(END, 'Dose: \t\t\t' + dose.get() + "\n")
            self.txtPrescription.insert(END, 'Number Of Tablets: \t\t\t' + numberTablets.get() + "\n")
            self.txtPrescription.insert(END, 'Lot: \t\t\t' + lot.get() + "\n")
            self.txtPrescription.insert(END, 'Issued Date: \t\t\t' + issueDate.get() + "\n")
            self.txtPrescription.insert(END, 'Exp. Date: \t\t\t' + expDate.get() + "\n")
            self.txtPrescription.insert(END, 'Daily Dose: \t\t\t' + dailyDose.get() + "\n")
            self.txtPrescription.insert(END, 'Possible Side Effects: \t\t\t' + possibleSideEffects.get() + "\n")
            self.txtPrescription.insert(END, 'Further Information: \t\t\t' + furtherInfomation.get() + "\n")
            self.txtPrescription.insert(END, 'Storage Advice: \t\t\t' + storageAdvice.get() + "\n")
            self.txtPrescription.insert(END, 'Driving or Using Machine: \t\t\t' + drivingUsingMachine.get() + "\n")
            self.txtPrescription.insert(END, 'How To Use Medication: \t\t\t' + howtoUseMedication.get() + "\n")
            self.txtPrescription.insert(END, 'Patient ID: \t\t\t' + patientID.get() + "\n")
            self.txtPrescription.insert(END, 'NHS Number: \t\t\t' + patientNHSNO.get() + "\n")
            self.txtPrescription.insert(END, 'Patient Name: \t\t\t' + patientName.get() + "\n")
            self.txtPrescription.insert(END, 'Date of Birth: \t\t\t' + dateOfBirth.get() + "\n")
            self.txtPrescription.insert(END, 'Patient Address: \t\t\t' + patientAddress.get() + "\n")
            return

        # ==================================frame ====================================

        main_frame = Frame(self.root)
        main_frame.grid(row=800, column=800)

        titleFrame = Frame(main_frame, bd=5, width=1350, padx=20, relief=RIDGE)
        titleFrame.pack(side=TOP)

        self.lblTitle = Label(titleFrame, width=39, font=('arial', 40, 'bold', ),
                              text="Cor Marie Hospital Management System", justify=CENTER,
                              )
        self.lblTitle.grid(padx=2)

        frameDetail = Frame(main_frame, bd=5, width=1350, height=100, padx=20, relief=RIDGE)
        frameDetail.pack(side=BOTTOM)

        buttonFrame = Frame(main_frame, bd=0, width=1350, height=50, padx=20, relief=RIDGE)
        buttonFrame.pack(side=BOTTOM)

        dataFrame = Frame(main_frame, bd=5, width=1350, height=400, padx=20, relief=RIDGE)
        dataFrame.pack(side=BOTTOM)

        dataFrameLeft = LabelFrame(dataFrame, bd=5, width=800, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Patient Information:", )
        dataFrameLeft.pack(side=LEFT)

        dataFrameRight = LabelFrame(dataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE,
                                    font=('arial', 12, 'bold'), text="prescription:", )
        dataFrameRight.pack(side=RIGHT)

        # ==================================Data Frame Left====================================
        self.lblNameTablet = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Name of Tablets:", padx=2, pady=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

        self.cboNameTablet = ttk.Combobox(dataFrameLeft,
                                          textvariable=cmbNameTablets,
                                          state='readonly',
                                          font=('arial', 12, 'bold'), width=23)
        self.cboNameTablet['value'] = ('', 'ibuprofen', 'co-codamol', 'paracetamol', 'Luonart')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)

        self.lblFurtherInfo = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Further Information:", padx=2,
                                    pady=2)
        self.lblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFurtherInfo = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=furtherInfomation, width=25)
        self.txtFurtherInfo.grid(row=0, column=3)

        self.lblRef = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Reference No:", padx=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=ref, width=25)
        self.txtRef.grid(row=1, column=1)

        self.lblStorage = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Storage Advice:", padx=2, pady=2)
        self.lblStorage.grid(row=1, column=2, sticky=W)
        self.txtStorage = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=storageAdvice, width=25)
        self.txtStorage.grid(row=1, column=3)

        self.lblDose = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Dose:", padx=2, pady=2)
        self.lblDose.grid(row=2, column=0, sticky=W)
        self.txtDose = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=dose, width=25)
        self.txtDose.grid(row=2, column=1)

        self.lblDuseMachine = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Driving Machine:", padx=2, pady=2)
        self.lblDuseMachine.grid(row=2, column=2, sticky=W)
        self.txtDuseMachine = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=drivingUsingMachine,
                                    width=25)
        self.txtDuseMachine.grid(row=2, column=3)

        self.lblNoOfTablet = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="No Of Tablets: ", padx=2, pady=2)
        self.lblNoOfTablet.grid(row=3, column=0, sticky=W)
        self.txtNoOfTablet = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=numberTablets,
                                   width=25)
        self.txtNoOfTablet.grid(row=3, column=1)

        self.lblUseMedication = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Use Medication: ", padx=2,
                                      pady=2)
        self.lblUseMedication.grid(row=3, column=2, sticky=W)
        self.txtUseMedication = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=howtoUseMedication,
                                      width=25)
        self.txtUseMedication.grid(row=3, column=3)

        self.lblLot = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Lot: ", padx=2, pady=2)
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=lot,
                            width=25)
        self.txtLot.grid(row=4, column=1)

        self.lblPatientID = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Patient ID: ", padx=2, pady=2)
        self.lblPatientID.grid(row=4, column=2, sticky=W)
        self.txtPatientID = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=patientID,
                                  width=25)
        self.txtPatientID.grid(row=4, column=3)

        self.lblIssueDate = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Issued Date: ", padx=2, pady=2)
        self.lblIssueDate.grid(row=5, column=0, sticky=W)
        self.txtIssueDate = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=issueDate, state='readonly',
                                  width=25)
        self.txtIssueDate.grid(row=5, column=1)

        self.lblNHSNumber = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="NHS Number: ", padx=2, pady=2)
        self.lblNHSNumber.grid(row=5, column=2, sticky=W)
        self.txtNHSNumber = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=patientNHSNO,
                                  width=25)
        self.txtNHSNumber.grid(row=5, column=3)

        self.lblExpDate = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Exp Date: ", padx=2, pady=2)
        self.lblExpDate.grid(row=6, column=0, sticky=W)
        self.txtExpDate = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=expDate,
                                width=25)
        self.txtExpDate.grid(row=6, column=1)

        self.lblPatientName = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Patient Name: ", padx=2, pady=2)
        self.lblPatientName.grid(row=6, column=2, sticky=W)
        self.txtPatientName = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=patientName,
                                    width=25)
        self.txtPatientName.grid(row=6, column=3)

        self.lblDailyDose = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Daily Dose: ", padx=2, pady=2)
        self.lblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=dailyDose,
                                  width=25)
        self.txtDailyDose.grid(row=7, column=1)

        self.lblDateOfBirth = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Date of Birth: ", padx=2, pady=2)
        self.lblDateOfBirth.grid(row=7, column=2, sticky=W)
        self.txtDateOfBirth = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=dateOfBirth,
                                    width=25)
        self.txtDateOfBirth.grid(row=7, column=3)

        self.lblSideEffect = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Side Effect: ", padx=2, pady=2)
        self.lblSideEffect.grid(row=8, column=0, sticky=W)
        self.txtSideEffect = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=possibleSideEffects,
                                   width=25)
        self.txtSideEffect.grid(row=8, column=1)

        self.lblPatientAddress = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Patient Address: ", padx=2,
                                       pady=2)
        self.lblPatientAddress.grid(row=8, column=2, sticky=W)
        self.txtPatientAddress = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=patientAddress,
                                       width=25)
        self.txtPatientAddress.grid(row=8, column=3)

        self.lblRandom = Label(dataFrameLeft, font=('arial', 12, 'bold'), text="Random: ", padx=2,
                               pady=2)
        self.lblRandom.grid(row=9, column=0, sticky=W)
        self.txtRandom = Entry(dataFrameLeft, font=('arial', 12, 'bold'), textvariable=patientAddress,
                               width=25)
        self.txtRandom.grid(row=9, column=1)

        # ==================================Data Frame Right====================================

        self.txtPrescription = Text(dataFrameRight, font=('arial', 12, 'bold'), width=45, height=11.4, padx=2,
                                    pady=2)
        self.txtPrescription.grid(row=0, column=0)

        # ==================================Button Frame==========================================
        self.btnPrescription = Button(buttonFrame, text="Prescription", font=('arial', 12, 'bold'), width=24, bd=4,
                                      command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)

        self.btnPrescriptionData = Button(buttonFrame, text="Prescription Data", font=('arial', 12, 'bold'), width=24,
                                          bd=4,
                                          command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=1)

        self.btnDelete = Button(buttonFrame, text="Delete", font=('arial', 12, 'bold'), width=17, bd=4, command=iDelete)
        self.btnDelete.grid(row=0, column=2)

        self.btnReset = Button(buttonFrame, text="Reset", font=('arial', 12, 'bold'), width=17, bd=4, command=iReset)
        self.btnReset.grid(row=0, column=3)

        self.btnPrint = Button(buttonFrame, text="Print", font=('arial', 12, 'bold'), width=17, bd=4)
        self.btnPrint.grid(row=0, column=4)

        self.btnExit = Button(buttonFrame, text="Exit", font=('arial', 12, 'bold'), width=17, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=5)

        # ==================================frame Detail==========================================
        self.lblLabel = Label(frameDetail, font=('arial', 10, 'bold'), pady=10,
                              text="Name of Tablets"
                                   "\t Reference No."
                                   "\t Dosage"
                                   "\t No of Tablets"
                                   "\t Lot"
                                   "\t Issued Date "
                                   "\t Exp. Date"
                                   "\t Daily Dose"
                                   "\t Storage"
                                   "\t NHS Number"
                                   "\t Patient Name"
                                   "\t DOB"
                                   "\t Address")
        self.lblLabel.grid(row=0, column=0)

        self.texFrameDetail = Text(frameDetail, font=('arial', 12, 'bold'), width=141, height=4, padx=2,
                                   pady=4)
        self.texFrameDetail.grid(row=1, column=0)


if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()
