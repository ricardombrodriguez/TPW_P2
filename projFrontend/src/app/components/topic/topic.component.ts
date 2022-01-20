import { Component, Input, OnInit } from '@angular/core';
import { Publication_Topics } from 'src/app/interfaces/publication_topics';

@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.css']
})
export class TopicComponent implements OnInit {

  @Input() topic!: Publication_Topics;

  constructor() { }

  ngOnInit(): void {
  }

}
