package com.example.fragment2;

import static com.example.fragment2.CarritoActual.precioFinal;
import static com.example.fragment2.CarritoActual.titleGames;

import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class Adapter extends RecyclerView.Adapter<Adapter.ViewHolder> {

    List<String> gamesTitles;
    List<String> gamesPrices;
    List<Integer> gamesImages;
    private Context mcontext;

    public Adapter(Context ctx, List<String> titles, List<String> prices, List<Integer> images){
        gamesTitles = titles;
        gamesPrices = prices;
        gamesImages = images;
        mcontext = ctx;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.game_list_custom, parent, false);
        return new ViewHolder (view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        holder.gameTitle.setText(gamesTitles.get(position));
        holder.gamePrice.setText(gamesPrices.get(position));
        holder.gameBuy.setText("Comprar");
        holder.gameBuy.setOnClickListener(view -> {
            CarritoActual.titleGames.add(gamesTitles.get(position));
            CarritoActual.precioFinal = CarritoActual.precioFinal + Integer.parseInt(gamesPrices.get(position));
            Log.d("pepe", gamesTitles.get(position));
            Log.d("pepe", ""+CarritoActual.precioFinal);
        });
        holder.gameImage.setImageResource(gamesImages.get(position));
    }

    @Override
    public int getItemCount() {
        return gamesTitles.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{

        TextView gameTitle;
        TextView gamePrice;
        Button gameBuy;
        ImageView gameImage;

        public ViewHolder(@NonNull View itemView){
            super(itemView);
            gameTitle = itemView.findViewById(R.id.titulo);
            gamePrice = itemView.findViewById(R.id.precio);
            gameBuy = itemView.findViewById(R.id.comprar);
            gameImage = itemView.findViewById(R.id.image);
        }


    }

}
