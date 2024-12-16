package com.bulbula.game;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private TextView
            mMenuOption_Start = null,
            mMenuOption_Sound = null,
            mMenuOption_Options = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initResources();
    }

    /**
     * To initialize the resources with the specified resource ID
     */
    private void initResources() {
        mMenuOption_Start = findViewById(R.id.mainActivity_menuOption_Start);
        mMenuOption_Sound = findViewById(R.id.mainActivity_menuOption_Sound);
        mMenuOption_Options = findViewById(R.id.mainActivity_menuOption_Options);
        mMenuOption_Start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent mStartGameIntent = new Intent(MainActivity.this, StartActivity.class);
                mStartGameIntent.putExtra("launchGame", "new");
                startActivity(mStartGameIntent);
            }
        });
    }

}
