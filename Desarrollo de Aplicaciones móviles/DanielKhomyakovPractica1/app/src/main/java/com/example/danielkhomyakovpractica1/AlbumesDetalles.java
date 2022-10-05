package com.example.danielkhomyakovpractica1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

public class AlbumesDetalles extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_albumes_detalles);
        long albumName = (long) getIntent().getExtras().get("ALBUM_ID");
        AlbumesDetallesFragment fragment = (AlbumesDetallesFragment) getSupportFragmentManager().findFragmentById(R.id.album_detail_fragment);
        setTitle(Albumes.AlbumesData.m_AlbumesData.get((int)albumName).m_ALbumName);
        fragment.setGroup(albumName);

    }
}