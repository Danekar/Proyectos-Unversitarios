package com.example.danielkhomyakovpractica1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import java.util.ArrayList;
import java.util.List;

public class Grupos extends AppCompatActivity implements GruposLista.Listener {

@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        GrupoData auxData = new GrupoData("Grandson");
        GrupoData.m_grupoDataList.add(auxData);
        auxData = new GrupoData("Sub Urban");
        GrupoData.m_grupoDataList.add(auxData);
        auxData = new GrupoData("The White Stripes");
        GrupoData.m_grupoDataList.add(auxData);
        setContentView(R.layout.activity_main);
        }

@Override
public void itemClicked (long id)
        {
        Intent intent = new Intent(this, Albumes.class);
        intent.putExtra("DETAIL_ID", (int)id);
        startActivity(intent);
        }

public static class GrupoData
{
    public String m_GrupoName;
    public static final List<GrupoData> m_grupoDataList = new ArrayList<GrupoData>();
    public GrupoData(String GrupoName)
    {
        m_GrupoName = GrupoName;
    }
}

}