import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FavouriteComponent } from './components/favourite/favourite.component';
import { PublicationComponent } from './components/publication/publication.component';
import { TopicComponent } from './components/topic/topic.component';
import { ActivePublicationsComponent } from './pages/active-publications/active-publications.component';
import { ClosedPublicationsComponent } from './pages/closed-publications/closed-publications.component';
import { CreatePublicationComponent } from './pages/create-publication/create-publication.component';
import { LoginComponent } from './pages/login/login.component';
import { ManageUsersComponent } from './pages/manage-users/manage-users.component';
import { MyPublicationsComponent } from './pages/my-publications/my-publications.component';
import { PendentPublicationsComponent } from './pages/pendent-publications/pendent-publications.component';
import { RegisterComponent } from './pages/register/register.component';

const routes: Routes = [

  { path: '', component: ActivePublicationsComponent },

  { path: 'login', component: LoginComponent },

  { path: 'register', component: RegisterComponent },

  { path: 'my_publications', component: MyPublicationsComponent },

  { path: 'pendent_publications', component: PendentPublicationsComponent },

  { path: 'closed_publications', component: ClosedPublicationsComponent },

  { path: 'favourites', component: FavouriteComponent },

  { path: 'users', component: ManageUsersComponent },

  { path: 'topics', component: TopicComponent },

  { path: 'publication/:id', component: PublicationComponent },

  { path: 'create_publication', component: CreatePublicationComponent },

];

@NgModule({
  declarations: [],
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
