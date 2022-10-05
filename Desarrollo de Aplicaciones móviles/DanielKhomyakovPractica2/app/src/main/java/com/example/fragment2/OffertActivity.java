package com.example.fragment2;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.os.Bundle;
import android.util.Log;
import android.view.MenuItem;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.navigation.NavigationView;

import java.util.ArrayList;
import java.util.List;

public class OffertActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener  {

    RecyclerView gameList;
    Adapter adapter2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_offert);
        gameList = findViewById(R.id.gameRecyclerView);



        androidx.appcompat.widget.Toolbar toolbar = findViewById(R.id.toolbar2);
        setSupportActionBar(toolbar);

        DrawerLayout drawerLayout = (DrawerLayout) findViewById(R.id.drawerLayout2);
        Log.d("pepe", "yo soy: "+drawerLayout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this,
                drawerLayout,
                toolbar,
                0,
                0
        );
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.navigationdrawer_view);
        navigationView.setNavigationItemSelectedListener(this);

        SQLiteOpenHelper gameDbHelper = new GameDataHelper(this) ;
        SQLiteDatabase db = gameDbHelper.getReadableDatabase();
        Cursor cursor = db.query("GAMES",
                new String[] {"_id", "TITLE", "PRICE", "IMAGE_ID"},
                "OFFERT = true",
                null,
                null, null, null);
        List<String> gamesTitles = new ArrayList<>();
        List<String> gamesPrices = new ArrayList<>();
        List<Integer> gamesImages = new ArrayList<>();
        if (cursor.moveToFirst()){
            do{
                @SuppressLint("Range") String dataTitle = cursor.getString(cursor.getColumnIndex("TITLE"));
                gamesTitles.add(dataTitle);
                Log.d("AG", dataTitle);
            }while(cursor.moveToNext());
            cursor.moveToPosition(0);
            do{
                @SuppressLint("Range") String dataPrice = cursor.getString(cursor.getColumnIndex("PRICE"));
                gamesPrices.add(dataPrice);
                Log.d("AG", dataPrice);
            }while(cursor.moveToNext());
            cursor.moveToPosition(0);

            do{
                @SuppressLint("Range") int dataImage = cursor.getInt(cursor.getColumnIndex("IMAGE_ID"));
                gamesImages.add(dataImage);
                Log.d("AG", ""+dataImage);
            }while(cursor.moveToNext());

        }
        cursor.close();

        adapter2 = new Adapter(this, gamesTitles, gamesPrices, gamesImages);
        GridLayoutManager gridLayoutManager = new GridLayoutManager(this,2,GridLayoutManager.VERTICAL,false);
        gameList.setLayoutManager(gridLayoutManager);
        gameList.setAdapter(adapter2);

    }

    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        int id = item.getItemId();
        switch (id)
        {
            case R.id.navigation_juegos :
                Intent intentMenuJuegos = new Intent(this, MainActivity.class);
                startActivity(intentMenuJuegos);
                break;
            case R.id.navigation_carrito:
                Intent intentMenuCarrito = new Intent(this, CarritoActivity.class);
                startActivity(intentMenuCarrito);
                break;
            case R.id.navigation_ofertas:
                Intent intentMenuOfertas = new Intent(this, OffertActivity.class);
                startActivity(intentMenuOfertas);
                break;
        }
        DrawerLayout drawerLayout = (DrawerLayout) findViewById(R.id.drawerLayout2);
        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }



}
