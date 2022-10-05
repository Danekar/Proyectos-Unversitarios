package com.example.danielkhomyakovpractica1;

import android.content.Context;
import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.ListFragment;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;

public class AlbumesLista extends ListFragment {
    public long m_IDGroup;
    public ArrayAdapter<String> adapter;
    public ArrayList<String> names;
    public AlbumesLista() {
// Required empty public constructor
    }

    public void setGroup (long id) {
        m_IDGroup = id;
        names= new ArrayList<>();
        for (int k = 0; k < Albumes.AlbumesData.m_AlbumesData.size(); k++) {
            if (m_IDGroup == Albumes.AlbumesData.m_AlbumesData.get(k).m_IDGrupo) {
                names.add(Albumes.AlbumesData.m_AlbumesData.get(k).m_ALbumName);
            }
        }
        //((LinearLayout) findViewById(android.R.id.simple_list_item_1)).removeAllViews();
        adapter = new ArrayAdapter<>(getContext(), android.R.layout.simple_list_item_1, names);
        setListAdapter(adapter);

    }

    interface Listener {
        void itemClicked(long id);
    }
    private AlbumesLista.Listener m_listener;

    @Override
    public void onAttach(Context context)
    {
        super.onAttach(context);
        m_listener = (AlbumesLista.Listener) context;
    }

    @Override
    public void onListItemClick(ListView list, View item, int position, long id)
    {
        if (m_listener != null)
        {
            m_listener.itemClicked(id);
        }
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        return super.onCreateView(inflater, container, savedInstanceState);
    }
}