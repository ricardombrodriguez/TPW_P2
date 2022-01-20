import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/interfaces/user';
import { UsersService } from 'src/app/services/users.service';

@Component({
  selector: 'app-manage-users',
  templateUrl: './manage-users.component.html',
  styleUrls: ['./manage-users.component.css']
})
export class ManageUsersComponent implements OnInit {

  public users!: User[];

  constructor(private userService: UsersService) { }

  ngOnInit(): void {

    this.getAllUsers();

  }

  getAllUsers() {
    return this.userService.getUsers().subscribe((users) => {
      this.users = users;
    })
  }

}
