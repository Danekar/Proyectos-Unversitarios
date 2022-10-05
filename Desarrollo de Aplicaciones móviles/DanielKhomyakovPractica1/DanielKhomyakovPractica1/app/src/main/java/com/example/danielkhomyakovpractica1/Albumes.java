package com.example.danielkhomyakovpractica1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.util.Log;
import android.widget.LinearLayout;

import java.util.ArrayList;
import java.util.List;



public class Albumes extends AppCompatActivity implements AlbumesLista.Listener {
    public int groupID;


    @Override
    protected void onCreate(Bundle savedInstanceState) {

        comprobadorDeAlbumes();
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_albumes);
        groupID = (int) getIntent().getExtras().get("DETAIL_ID");
        AlbumesLista fragment = (AlbumesLista) getSupportFragmentManager().findFragmentById(R.id.fragment_albumes_lista);
        Log.d("1", "id de grupos: "+groupID);
        // ((LinearLayout) findViewById(R.id.simple_list_item_1)).removeAllViews();
        fragment.setGroup(groupID);
    }

    private void comprobadorDeAlbumes() {
        if(AlbumesData.m_AlbumesData.isEmpty()){
            Log.d("1","he creado albumes");
            createAlbumes();
        }else{
            Log.d("1","no tengo que crear albumes");
        }
    }

    @Override
    public void itemClicked (long id)
    {
        Intent intent = new Intent(this, AlbumesDetalles.class);
        for (int i =0;i<Albumes.AlbumesData.m_AlbumesData.size(); i++){
            if(AlbumesData.m_AlbumesData.get(i).m_IDGrupo==groupID){
                intent.putExtra("ALBUM_ID", id);
                startActivity(intent);
                break;
            }
            id++;
        }

        }

        public void createAlbumes(){
            AlbumesData auxData = new AlbumesData(0,"Death of an Optimist", "2020", "Identity, Dirty", R.drawable.death_of_an_optimist);
            AlbumesData.m_AlbumesData.add(auxData);
            auxData = new AlbumesData(0,"A Modern Tragedy Vol. 1", "2018", "Blood // Water, despicable", R.drawable.a_modern_tragedy_vol_1);
            AlbumesData.m_AlbumesData.add(auxData);
            auxData = new AlbumesData(0,"A Modern Tragedy Vol. 2", "2019", "Apologize, Darkside", R.drawable.a_modern_tragedy_vol_2);
            AlbumesData.m_AlbumesData.add(auxData);

            auxData = new AlbumesData(1,"Definition Forbiden", "2019", "No Way Out, Olifant", R.drawable.definition_forbiden);
            AlbumesData.m_AlbumesData.add(auxData);
            auxData = new AlbumesData(1,"Thrill Seeker", "2020", "Freak, Cliche", R.drawable.thril_seeker);
            AlbumesData.m_AlbumesData.add(auxData);

            auxData = new AlbumesData(2,"Elephant", "2003", "Seven Nation Army, Black Math", R.drawable.elephant);
            AlbumesData.m_AlbumesData.add(auxData);
            auxData = new AlbumesData(2,"Icky Thump", "2007", "Conquest, Bone Broke", R.drawable.icky_thump);
            AlbumesData.m_AlbumesData.add(auxData);
            auxData = new AlbumesData(2,"White Blood Cells", "2001", "Hotel Yorba, Fell in Love With a Girl", R.drawable.white_blood_cells);
            AlbumesData.m_AlbumesData.add(auxData);
        }

    public static class AlbumesData
    {
        public long m_IDGrupo;
        public String m_ALbumName;
        public String m_Fecha;
        public String m_Canciones;
        public int m_imageName;
        public static final List<AlbumesData> m_AlbumesData  = new ArrayList<>();


        public AlbumesData(int IDGrupo, String AlbumName, String Fecha, String Canciones, int imageName)
        {
            m_IDGrupo = IDGrupo;
            m_ALbumName = AlbumName;
            m_Fecha = Fecha;
            m_Canciones = Canciones;
            m_imageName = imageName;

        }
    }
}