import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Publication } from 'src/app/interfaces/publication';
import { PublicationService } from 'src/app/services/publication.service';

@Component({
  selector: 'app-active-publications',
  templateUrl: './active-publications.component.html',
  styleUrls: ['./active-publications.component.css']
})
export class ActivePublicationsComponent implements OnInit {

  public publications!: Publication[];

  constructor(private publicationsService: PublicationService) { }

  ngOnInit(): void {

    this.getActivePublications();

  }

  getActivePublications(): void {
    this.publicationsService.getActivePublications().subscribe((publications) => {
      this.publications = publications;
    });
  }

}
