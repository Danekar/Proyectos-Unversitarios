package com.example.fragment2;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.viewpager.widget.ViewPager;

import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;

import com.google.android.material.navigation.NavigationView;
import com.google.android.material.tabs.TabLayout;

public class MainActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        CatPagerAdapter adapter = new CatPagerAdapter(getSupportFragmentManager(), this);
        ViewPager pager = findViewById(R.id.viewpager1);
        //Log.d("2", "yo soy: "+pager);
        pager.setAdapter(adapter);

        androidx.appcompat.widget.Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        TabLayout tabLayout = (TabLayout) findViewById(R.id.tablayout);
        tabLayout.setupWithViewPager(pager);

        DrawerLayout drawerLayout = (DrawerLayout) findViewById(R.id.drawerLayout);
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

    }

    public void comprarJuegos(View v){

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
            DrawerLayout drawerLayout = (DrawerLayout) findViewById(R.id.drawerLayout);
            drawerLayout.closeDrawer(GravityCompat.START);
            return true;
    }
}