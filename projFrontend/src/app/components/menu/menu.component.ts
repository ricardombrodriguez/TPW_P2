import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  token = localStorage.getItem('token');
  loggedIn = true ? this.token != null : false 
  username = localStorage.getItem('username');
  group=localStorage.getItem('group');
  constructor() { }

  ngOnInit(): void {
  }

  logout(){
    localStorage.clear()
    this.loggedIn=false
    window.location.href=''
  }
}
