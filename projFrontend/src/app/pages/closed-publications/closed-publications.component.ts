import { Component, OnInit } from '@angular/core';
import { Publication } from 'src/app/interfaces/publication';
import { PublicationService } from 'src/app/services/publication.service';

@Component({
  selector: 'app-closed-publications',
  templateUrl: './closed-publications.component.html',
  styleUrls: ['./closed-publications.component.css']
})
export class ClosedPublicationsComponent implements OnInit {

  public publications!: Publication[];

  constructor(private publicationsService: PublicationService) { }

  ngOnInit(): void {

    this.getClosedPublications();

  }

  getClosedPublications(): void {
    this.publicationsService.getClosedPublications().subscribe((publications) => {
      this.publications = publications;
    });
  }

}
