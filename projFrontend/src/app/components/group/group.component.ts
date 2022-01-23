import { Component, Input, OnInit } from '@angular/core';
import { Group } from 'src/app/interfaces/group';
import { User } from 'src/app/interfaces/user';
import { UsersService } from 'src/app/services/users.service';

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {

  @Input() user!: User;
  public groups!: Group[];
  token=''+localStorage.getItem("token")
  constructor(private userSService: UsersService) { }

  ngOnInit(): void {

    this.getGroups();

  }

  getGroups() {
    return this.userSService.getGroups(this.token).subscribe((groups) => {
      console.log(groups)
      this.groups = groups;
    })
  }

}
