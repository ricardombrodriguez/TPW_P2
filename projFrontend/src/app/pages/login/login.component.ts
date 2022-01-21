import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Location } from '@angular/common';
import { FormBuilder, FormGroup } from '@angular/forms';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  token = ""
  showError = false

  constructor(private fb:FormBuilder, private loginService: LoginService, private location:Location) { }

  contactForm !:FormGroup;

  ngOnInit(): void {

    console.log("oi")

    this.contactForm = this.fb.group({
      username: [null],
      password:[null],
    });

  }

  public submit(): void{
    this.showError = false
    console.log(this.contactForm.value)
    this.loginService.logIn(this.contactForm.value["username"], this.contactForm.value["password"]).
    subscribe(
      data => {
          console.log('Success: ', data);

          let data_json = JSON.parse(JSON.stringify(data))

          this.token = data_json.token;
          console.log(this.token)
          localStorage.setItem('token', this.token);
          localStorage.setItem('username', this.contactForm.value["username"]);
          //SERRAS
          localStorage.setItem('id', "3");
          localStorage.setItem('group', "Admin");
          //SERRAS
          this.location.back();
      },
      error => {
          console.log('Error: ', error);
          // this.token = {};
          this.showError = true
          this.contactForm = this.fb.group({
            username: [null],
            password:[null],
          });
      });
  }

}
