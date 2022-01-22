import { THIS_EXPR } from '@angular/compiler/src/output/output_ast';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Favorite } from 'src/app/interfaces/favorite';
import { Publication } from 'src/app/interfaces/publication';
import { User } from 'src/app/interfaces/user';
import { FavoriteService } from 'src/app/services/favorite.service';
import { PublicationService } from 'src/app/services/publication.service';

@Component({
  selector: 'app-publication-page',
  templateUrl: './publication-page.component.html',
  styleUrls: ['./publication-page.component.css']
})
export class PublicationPageComponent implements OnInit {

  public id!: number;
  public pub!: Publication;
  public group = localStorage.getItem("group")
  token = localStorage.getItem('token');
  loggedIn = true ? this.token != null : false 
  username = localStorage.getItem('username');
  user_id:number=-1
  isFav : boolean =false
  public user = new User();
  constructor(private publicationService: PublicationService, private router: Router,private favoriteService:FavoriteService) { }

  ngOnInit(): void {
    var str_id =localStorage.getItem(('id'))
    if (str_id==null){
      str_id='-1'
    }
    this.user_id =+str_id
    const url_array = this.router.url.split("/");
    this.id = +url_array[url_array.length - 1];
    this.getPublicationDetails();
    console.log("OLAAAAAAAA")
    console.log("OLAAAAAAAA")

  }

  getPublicationDetails() {
    return this.publicationService.getPublication(this.id).subscribe((pub) => {
      this.pub = pub;

      
      this.favoriteService.checkIfFavorite(this.user_id,this.pub.id).subscribe(
        data => {
          this.isFav=true
        },
        error =>{
            this.isFav=false
        });
      //metodo para ver se é favorito , se receber algo é se não é false
    
    })
  }
  

}
