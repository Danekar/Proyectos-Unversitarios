package com.example.fragment2;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.navigation.NavigationView;

import org.w3c.dom.Text;

import java.util.ArrayList;
import java.util.List;

public class CarritoActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener  {

    private ListView listview;
    private TextView precioTotal;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_carrito);
        listview = (ListView) findViewById(R.id.listView);
        precioTotal = findViewById(R.id.totalPrecio);
        //Log.d("ep", "onCreate: "+precioTotal);
        precioTotal.setText(""+CarritoActual.precioFinal+"$");


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

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, CarritoActual.titleGames);

        listview.setAdapter(adapter);

    }

    public void terminarCompra(View v){
        Intent intent = new Intent(Intent.ACTION_SEND);
        intent.putExtra(Intent.EXTRA_EMAIL,"danilaesp001@gmail.com");
        intent.putExtra(Intent.EXTRA_SUBJECT, "Compra juegos");
        intent.putExtra(Intent.EXTRA_TEXT, "Los juegos que usted quiere comprar son: "+CarritoActual.titleGames+"\n"+"El precio total de estos son: "+CarritoActual.precioFinal+"$");
        intent.setType("message/rfc822");
        startActivity(Intent.createChooser(intent, "Choose an Email client :"));
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
