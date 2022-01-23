import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  registerForm !:FormGroup;
  showUsernameError:Boolean = false;
  showFirstNameError:Boolean = false;
  showPasswordError:Boolean = false;
  showConfirmPasswordError:Boolean = false;

  constructor(private fb:FormBuilder, private registService: AuthenticationService, private location:Location) { }

  ngOnInit(): void {
    this.registerForm = this.fb.group({
      username: [null],
      first_name: [null],
      last_name: [null],
      password:[null],
      confirm_password:[null]
    });
  }

  public submit(): void {
    this.showUsernameError = false;
    this.showFirstNameError = false;
    this.showPasswordError = false;
    this.showConfirmPasswordError = false;
    
    console.log(this.registerForm.value)

    if (this.registerForm.value["username"] === null || this.registerForm.value["username"].trim() === "") {
      console.log("erro")
      this.showUsernameError = true;
    }

    if (this.registerForm.value["first_name"] === null || this.registerForm.value["first_name"].trim() === "") {
      console.log("erro")
      this.showFirstNameError = true;
    }

    if (this.registerForm.value["password"] === null || this.registerForm.value["password"].trim() === "") {
      console.log("erro")
      this.showPasswordError = true;
    }

    if (this.registerForm.value["confirm_password"] != this.registerForm.value["password"]) {
      console.log("erro, password")
      this.showConfirmPasswordError = true;
    }
  }

}
