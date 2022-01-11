import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { MenuComponent } from './components/menu/menu.component';
import { SearchComponent } from './components/search/search.component';
import { PublicationComponent } from './components/publication/publication.component';
import { TopicComponent } from './components/topic/topic.component';
import { FavouriteComponent } from './components/favourite/favourite.component';
import { UserComponent } from './components/user/user.component';
import { GroupComponent } from './components/group/group.component';
import { RegisterComponent } from './pages/register/register.component';
import { LoginComponent } from './pages/login/login.component';
import { MyPublicationsComponent } from './pages/my-publications/my-publications.component';
import { ActivePublicationsComponent } from './pages/active-publications/active-publications.component';
import { PendentPublicationsComponent } from './pages/pendent-publications/pendent-publications.component';
import { ClosedPublicationsComponent } from './pages/closed-publications/closed-publications.component';
import { FavouritesComponent } from './pages/favourites/favourites.component';
import { ManageUsersComponent } from './pages/manage-users/manage-users.component';
import { ManageTopicsComponent } from './pages/manage-topics/manage-topics.component';
import { CreatePublicationComponent } from './pages/create-publication/create-publication.component';
import { CommentComponent } from './components/comment/comment.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    SearchComponent,
    PublicationComponent,
    TopicComponent,
    FavouriteComponent,
    UserComponent,
    GroupComponent,
    RegisterComponent,
    LoginComponent,
    MyPublicationsComponent,
    ActivePublicationsComponent,
    PendentPublicationsComponent,
    ClosedPublicationsComponent,
    FavouritesComponent,
    ManageUsersComponent,
    ManageTopicsComponent,
    CreatePublicationComponent,
    CommentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }