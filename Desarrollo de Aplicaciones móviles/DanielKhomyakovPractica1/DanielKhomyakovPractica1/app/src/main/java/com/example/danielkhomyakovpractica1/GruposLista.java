package com.example.danielkhomyakovpractica1;

import android.content.Context;
import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.ListFragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class GruposLista extends ListFragment {

    public GruposLista() {
// Required empty public constructor
    }

    interface Listener {
        void itemClicked(long id);
    }
    private Listener m_listener;

    @Override
    public void onAttach(Context context)
    {
        super.onAttach(context);
        m_listener = (Listener) context;
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
        String names[] = new String[Grupos.GrupoData.m_grupoDataList.size()];
        for (int i = 0; i < Grupos.GrupoData.m_grupoDataList.size(); i++)
        {
            names[i] = Grupos.GrupoData.m_grupoDataList.get(i).m_GrupoName;
        }
        ArrayAdapter<String> adapter = new ArrayAdapter<>(inflater.getContext(), android.R.layout.simple_list_item_1, names);
        setListAdapter(adapter);
        return super.onCreateView(inflater, container, savedInstanceState);
    }


}