import { Component, OnInit } from '@angular/core';
import { Publication } from 'src/app/interfaces/publication';
import { PublicationService } from 'src/app/services/publication.service';

@Component({
  selector: 'app-favourites',
  templateUrl: './favourites.component.html',
  styleUrls: ['./favourites.component.css']
})
export class FavouritesComponent implements OnInit {

  public favourites!: Publication[];





  // só para testar!!!
  public userID: number = 1;





  constructor(private publicationService: PublicationService) { }

  ngOnInit(): void {

    this.getFavouritePublications(this.userID);

  }

  getFavouritePublications(id: number) {
    return this.publicationService.getFavouritePublicationsByUser(id).subscribe((favourites) => {
      this.favourites = favourites;
    })
  }

}
