import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Publication } from 'src/app/interfaces/publication';
import { PublicationService } from 'src/app/services/publication.service';

@Component({
  selector: 'app-publication-page',
  templateUrl: './publication-page.component.html',
  styleUrls: ['./publication-page.component.css']
})
export class PublicationPageComponent implements OnInit {

  public id!: number;
  public pub!: Publication;

  constructor(private publicationService: PublicationService, private router: Router) { }

  ngOnInit(): void {

    const url_array = this.router.url.split("/");
    this.id = +url_array[url_array.length - 1];
    this.getPublicationDetails();

  }

  getPublicationDetails() {
    return this.publicationService.getPublication(this.id).subscribe((pub) => {
      this.pub = pub;
    })
  }

}
