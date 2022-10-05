package com.example.fragment2;

import android.content.ContentValues;
import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import androidx.annotation.Nullable;

public class GameDataHelper extends SQLiteOpenHelper {

    private static final String DBNAME = "gamesdatabase";
    private static final int DBVERSION = 1;

    public GameDataHelper(Context context) {
        super(context, DBNAME, null, DBVERSION);
    }
    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE GAMES ("
                + "_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                + "TITLE TEXT, "
                + "CONSOLE TEXT, "
                + "OFFERT BOOLEAN, "
                + "PRICE INTEGER, "
                + "IMAGE_ID INTEGER); ");
        addVideogame (db, "Nier Automata", "Ps4", true, 25, R.drawable.niew_automata);
        addVideogame (db, "God Of War", "Ps4", false, 50, R.drawable.god_of_war);
        addVideogame (db, "Uncharted 4", "Ps4", true, 20, R.drawable.uncharted_4);

        addVideogame (db, "Gears Of War", "Xbox", false, 70, R.drawable.gears_of_war);
        addVideogame (db, "Assassins Creed Valhalla", "Xbox", true, 10, R.drawable.ac_valhala);
        addVideogame (db, "Halo 5", "Xbox", true, 15, R.drawable.halo_5);

        addVideogame (db, "Elden Ring", "PC", false, 60, R.drawable.elden_ring);
        addVideogame (db, "Starcraft2", "PC", true, 2, R.drawable.starcraft2);
        addVideogame (db, "Age Of Empire III", "PC", true, 5, R.drawable.age_of_empires);


    }
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
    }

    public static void addVideogame (SQLiteDatabase db, String title, String console, boolean oferta, int price, int gameImage)
    {
        ContentValues gamesData = new ContentValues();
        gamesData.put("TITLE", title);
        gamesData.put("CONSOLE", console);
        gamesData.put("OFFERT", oferta);
        gamesData.put("PRICE", price);
        gamesData.put("IMAGE_ID", gameImage);
        db.insert("GAMES", null, gamesData);
    }

}
