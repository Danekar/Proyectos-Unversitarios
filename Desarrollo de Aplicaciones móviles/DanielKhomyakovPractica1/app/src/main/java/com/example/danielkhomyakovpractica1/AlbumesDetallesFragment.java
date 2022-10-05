package com.example.danielkhomyakovpractica1;

import android.graphics.drawable.Drawable;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;


public class AlbumesDetallesFragment extends Fragment {
    private long m_albumName;
    public AlbumesDetallesFragment() {
// Required empty public constructor
    }
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
// Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_albumes_detalles, container, false);
    }
    public void setGroup (long id)
    {
        m_albumName= id;
        Log.d("1","Id de album es: " + m_albumName);
        View v = getView();
        if (v != null)
        {

            ((ImageView)v.findViewById(R.id.AlbumImagen)).setImageResource(Albumes.AlbumesData.m_AlbumesData.get((int)m_albumName).m_imageName);
            ((TextView)v.findViewById(R.id.AlbumName)).setText(Albumes.AlbumesData.m_AlbumesData.get((int)m_albumName).m_ALbumName);
            ((TextView)v.findViewById(R.id.AlbumFecha)).setText(Albumes.AlbumesData.m_AlbumesData.get((int)m_albumName).m_Fecha);
            ((TextView)v.findViewById(R.id.AlbumCanciones)).setText(Albumes.AlbumesData.m_AlbumesData.get((int)m_albumName).m_Canciones);

        }
    }

    public void onStart ()
    {
        super.onStart();

    }

}