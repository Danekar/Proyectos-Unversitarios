package com.example.fragment2;

import android.annotation.SuppressLint;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.ListFragment;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.util.ArrayList;
import java.util.List;


public class PcFragment extends Fragment {
    RecyclerView gameList;
    Adapter adapter;
    private static final String TAG = "RecyclerViewPcFragment";


    public PcFragment() {
        // Required empty public constructor
    }



    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View vista = inflater.inflate(R.layout.fragment_games_list_recycle_view, container, false);
        vista.setTag(TAG);
        gameList =  vista.findViewById(R.id.gameRecyclerView);
        SQLiteOpenHelper gameDbHelper = new GameDataHelper(getContext()) ;
        SQLiteDatabase db = gameDbHelper.getReadableDatabase();
        Cursor cursor = db.query("GAMES",
                new String[] {"_id", "TITLE", "PRICE", "IMAGE_ID"},
                "CONSOLE='PC'",
                null,
                null, null, null);
        List<String> gamesTitles = new ArrayList<>();
        List<String> gamesPrices = new ArrayList<>();
        List<Integer> gamesImages = new ArrayList<>();
        Log.d("1","He entrado al SetReclye View");
        if (cursor.moveToFirst()){
            do{
                @SuppressLint("Range") String dataTitle = cursor.getString(cursor.getColumnIndex("TITLE"));
                gamesTitles.add(dataTitle);
            }while(cursor.moveToNext());
            cursor.moveToPosition(0);
            do{
                @SuppressLint("Range") String dataPrice = cursor.getString(cursor.getColumnIndex("PRICE"));
                gamesPrices.add(dataPrice);
            }while(cursor.moveToNext());
            cursor.moveToPosition(0);

            do{
                @SuppressLint("Range") int dataImage = cursor.getInt(cursor.getColumnIndex("IMAGE_ID"));
                gamesImages.add(dataImage);
            }while(cursor.moveToNext());

        }
        cursor.close();
        adapter = new Adapter(getActivity(), gamesTitles, gamesPrices, gamesImages);
        RecyclerView.LayoutManager layoutManager=new GridLayoutManager(getActivity(),2);
        gameList.setLayoutManager(layoutManager);
        gameList.setAdapter(adapter);
        /* GridLayoutManager gridLayoutManager = new GridLayoutManager(getActivity(),2 ,GridLayoutManager.HORIZONTAL, false);
        //gridLayoutManager.setSpanSizeLookup(2);
        gameList.setLayoutManager(gridLayoutManager);
        gameList.setAdapter(adapter);*/

        // Inflate the layout for this fragment
        return vista;
    }
}