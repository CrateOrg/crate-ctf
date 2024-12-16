package com.bulbula.game;

import android.content.DialogInterface;
import android.graphics.Color;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewTreeObserver;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.bulbula.game.utils.HighScoreHelper;
import com.bulbula.game.utils.SimpleAlertDialog;
import com.bulbula.game.utils.SoundHelper;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class StartActivity extends AppCompatActivity implements Bubble.BubbleListener {

    private static final int MIN_ANIMATION_DELAY = 500;
    private static final int MAX_ANIMATION_DELAY = 1500;
    private static final int MIN_ANIMATION_DURATION = 1000;
    private static final int MAX_ANIMATION_DURATION = 8000;
    private static final int NUMBER_OF_PINS = 9;
    private static final int BUBBLE_PER_LEVEL = 10;

    private ViewGroup mContentView;
    private int[] mBubbleColors = new int[3];
    private int mNextColor, mScreenWidth, mScreenHeight;
    TextView mScoreDisplay, mLevelDisplay;
    private List<ImageView> mPinImages = new ArrayList<>();
    private List<Bubble> mBubbles = new ArrayList<>();
    Button mGoButton;

    private boolean mPlaying;
    private boolean mGameStopped = true;
    private int mLevel, mScore, mPinsUsed;
    private int mBubblesPopped;

    private ImageView
            mhealth_100 = null,
            mhealth_90 = null,
            mhealth_80 = null,
            mhealth_70 = null,
            mhealth_60 = null,
            mhealth_50 = null,
            mhealth_40 = null,
            mhealth_30 = null,
            mhealth_20 = null;

    private SoundHelper mSoundHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_start);

        mBubbleColors[0] = Color.argb(255, 255, 0, 0);
        mBubbleColors[1] = Color.argb(255, 0, 255, 0);
        mBubbleColors[2] = Color.argb(255, 0, 0, 255);

//        getWindow().setBackgroundDrawableResource(R.drawable.bubble_3);

        mContentView = (ViewGroup) findViewById(R.id.startActivityMainLayout);
        setToFullScreen();

        ViewTreeObserver viewTreeObserver = mContentView.getViewTreeObserver();
        if (viewTreeObserver.isAlive()) {
            viewTreeObserver.addOnGlobalLayoutListener(new ViewTreeObserver.OnGlobalLayoutListener() {
                @Override
                public void onGlobalLayout() {
                    mContentView.getViewTreeObserver().removeOnGlobalLayoutListener(this);
                    mScreenHeight = mContentView.getHeight();
                    mScreenWidth = mContentView.getWidth();
                }
            });
        }

        mContentView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                setToFullScreen();
            }
        });

        mScoreDisplay = (TextView) findViewById(R.id.textView_gameScore);
        mLevelDisplay = (TextView) findViewById(R.id.textView_gameLevel);
//        mPinImages.add((ImageView) findViewById(R.id.health_100));
//        mPinImages.add((ImageView) findViewById(R.id.health_90));
//        mPinImages.add((ImageView) findViewById(R.id.health_80));
//        mPinImages.add((ImageView) findViewById(R.id.health_70));
//        mPinImages.add((ImageView) findViewById(R.id.health_60));
//        mPinImages.add((ImageView) findViewById(R.id.health_50));
//        mPinImages.add((ImageView) findViewById(R.id.health_40));
//        mPinImages.add((ImageView) findViewById(R.id.health_30));
//        mPinImages.add((ImageView) findViewById(R.id.health_20));
        mhealth_100 = (ImageView) findViewById(R.id.health_100);
        mhealth_90 = (ImageView) findViewById(R.id.health_90);
        mhealth_80 = (ImageView) findViewById(R.id.health_80);
        mhealth_70 = (ImageView) findViewById(R.id.health_70);
        mhealth_60 = (ImageView) findViewById(R.id.health_60);
        mhealth_50 = (ImageView) findViewById(R.id.health_50);
        mhealth_40 = (ImageView) findViewById(R.id.health_40);
        mhealth_30 = (ImageView) findViewById(R.id.health_30);
        mhealth_20 = (ImageView) findViewById(R.id.health_20);
        mGoButton = (Button) findViewById(R.id.settings);

        updateDisplay();

        mSoundHelper = new SoundHelper(this);
        mSoundHelper.prepareMusicPlayer(this);

        mContentView.performClick();
        findViewById(R.id.settings).performClick();
        //Log.e("TAG", getResult(31337));
    }

    private void setToFullScreen() {

        ViewGroup rootLayout = (ViewGroup) findViewById(R.id.startActivityMainLayout);

        rootLayout.setSystemUiVisibility(View.SYSTEM_UI_FLAG_LOW_PROFILE
                | View.SYSTEM_UI_FLAG_FULLSCREEN
                | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
        );
    }


    @Override
    protected void onResume() {
        super.onResume();
        setToFullScreen();
    }

    private void startGame() {
        setToFullScreen();
        mScore = 0;
        mLevel = 0;
        mPinsUsed = 0;
        updateLivesOnStart();
//        for (ImageView pin : mPinImages) {
//            pin.setImageResource(R.drawable.ic_cards_heart);
//        }

        mGameStopped = false;
        startLevel();
        mSoundHelper.playMusic();
    }

    private void startLevel() {
        mLevel++;
        updateDisplay();
        BubbleLauncher bubbleLauncher = new BubbleLauncher();
        bubbleLauncher.execute(mLevel);
        mPlaying = true;
        mBubblesPopped = 0;
        mGoButton.setText("Stop Game");
    }

    private void finishLevel() {
//        Toast.makeText(this, String.format("You finished level %d", mLevel), Toast.LENGTH_SHORT)
//                .show();
        mPlaying = false;

        AlertDialog.Builder builder;
//        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
//            builder = new AlertDialog.Builder(StartActivity.this, android.R.style.Theme_DeviceDefault_Dialog);
//        } else {
        builder = new AlertDialog.Builder(StartActivity.this);
//        }

        builder.setTitle("Hurrah!! Level Up ")
                .setMessage("Continue to level " +
                        String.format("%d", mLevel + 1))
                .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int which) {
                        findViewById(R.id.settings).performClick();
                    }
                })
                .setNegativeButton(android.R.string.no, new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int which) {
                        onBackPressed();
                    }
                })
                .setIcon(android.R.drawable.star_big_on)
                .setCancelable(false)
                .show();


//        mGoButton.setText(String.format("Start level %d", mLevel + 1));
    }

    public void goButtonClickHandler(View view) {
        if (mPlaying) {
            gameOver(false);
        } else if (mGameStopped) {
            startGame();
        } else {
            startLevel();
        }
    }

    @Override
    public void popBubble(Bubble bubble, boolean userTouch) {

        mSoundHelper.playSound();

        mBubblesPopped++;

        mContentView.removeView(bubble);
        mBubbles.remove(bubble);

        if (userTouch) {
            mScore++;
        } else {
            mPinsUsed++;
            if (mPinsUsed <= NUMBER_OF_PINS) {
//                mPinImages.get(mPinsUsed - 1)
//                        .setImageResource(R.drawable.ic_heart_off);
                updateUserLiveLeft(mPinsUsed);
                Log.d("Suhaas", "mPinsUsed : " + mPinsUsed);
            }
            if (mPinsUsed == NUMBER_OF_PINS) {
                gameOver(true);
                return;
            } else {
                Toast.makeText(this, "Missed that one! " + mPinsUsed, Toast.LENGTH_SHORT).show();
            }
        }
        updateDisplay();

        if (mBubblesPopped == BUBBLE_PER_LEVEL) {
            finishLevel();
        }
    }


    private void gameOver(boolean allPinsUsed) {
        mSoundHelper.pauseMusic();
        Toast.makeText(this, "Game Over! " + getResult(mScore), Toast.LENGTH_SHORT).show();

        for (Bubble bubble : mBubbles) {
            mContentView.removeView(bubble);
            bubble.setPopped(true);
        }

        mBubbles.clear();
        mPlaying = false;
        mGameStopped = true;
        mGoButton.setText("Start Game");

        if (allPinsUsed) {
            if (HighScoreHelper.isTopScore(this, mScore)) {
                HighScoreHelper.setTopScore(this, mScore);

                SimpleAlertDialog dialog = SimpleAlertDialog.newInstance("New High Score!",
                        String.format("Your new high score is %d", mScore));
                dialog.show(getSupportFragmentManager(), null);
            }
        }
    }

    private void updateDisplay() {
        mScoreDisplay.setText(String.valueOf(mScore));
        mLevelDisplay.setText(String.valueOf(mLevel));
    }

    private void updateUserLiveLeft(int mPinsUsed) {
        switch (mPinsUsed) {
            case 1:
                mhealth_100.setVisibility(View.GONE);
                mhealth_90.setVisibility(View.VISIBLE);
                break;
            case 2:
                mhealth_90.setVisibility(View.GONE);
                mhealth_80.setVisibility(View.VISIBLE);
                break;
            case 3:
                mhealth_70.setVisibility(View.VISIBLE);
                break;
            case 4:
                mhealth_70.setVisibility(View.GONE);
                mhealth_60.setVisibility(View.VISIBLE);
                break;
            case 5:
                mhealth_60.setVisibility(View.GONE);
                mhealth_50.setVisibility(View.VISIBLE);
                break;
            case 6:
                mhealth_40.setVisibility(View.VISIBLE);
                break;
            case 7:
                mhealth_40.setVisibility(View.GONE);
                mhealth_30.setVisibility(View.VISIBLE);
                break;
            case 8:
                mhealth_30.setVisibility(View.GONE);
                mhealth_20.setVisibility(View.VISIBLE);
                break;
            case 9:
                break;
            default:
        }
    }

    private void updateLivesOnStart() {
        mhealth_100.setVisibility(View.VISIBLE);
        mhealth_90.setVisibility(View.GONE);
        mhealth_80.setVisibility(View.GONE);

        mhealth_70.setVisibility(View.VISIBLE);
        mhealth_60.setVisibility(View.GONE);
        mhealth_50.setVisibility(View.GONE);

        mhealth_40.setVisibility(View.VISIBLE);
        mhealth_30.setVisibility(View.GONE);
        mhealth_20.setVisibility(View.GONE);

    }

    @Override
    protected void onStop() {
        super.onStop();
        gameOver(false);
    }


    private class BubbleLauncher extends AsyncTask<Integer, Integer, Void> {

        @Override
        protected Void doInBackground(Integer... params) {

            if (params.length != 1) {
                throw new AssertionError(
                        "Expected 1 param for current level");
            }

            int level = params[0];
            int maxDelay = Math.max(MIN_ANIMATION_DELAY,
                    (MAX_ANIMATION_DELAY - ((level - 1) * 500)));
            int minDelay = maxDelay / 2;

            int bubblesLaunched = 0;
            while (mPlaying && bubblesLaunched < BUBBLE_PER_LEVEL) {

//              Get a random horizontal position for the next bubble
                Random random = new Random();
                if (mScreenWidth > 0) {
                    int xPosition = random.nextInt(mScreenWidth - 200);
                    publishProgress(xPosition);
                    bubblesLaunched++;
                }


//              Wait a random number of milliseconds before looping
                int delay = random.nextInt(minDelay) + minDelay;
                try {
                    Thread.sleep(delay);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            return null;

        }

        @Override
        protected void onProgressUpdate(Integer... values) {
            super.onProgressUpdate(values);
            int xPosition = values[0];
            launchBubble(xPosition);
        }

    }

    private void launchBubble(int x) {

        Bubble bubble = new Bubble(this, mBubbleColors[mNextColor], 150);
        mBubbles.add(bubble);

        if (mNextColor + 1 == mBubbleColors.length) {
            mNextColor = 0;
        } else {
            mNextColor++;
        }

//      Set bubble vertical position and dimensions, add to container
        bubble.setX(x);
        bubble.setY(mScreenHeight + bubble.getHeight());
        mContentView.addView(bubble);

//      Let 'er fly
        int duration = Math.max(MIN_ANIMATION_DURATION, MAX_ANIMATION_DURATION - (mLevel * 1000));
        bubble.releaseBubble(mScreenHeight, duration);

    }

    public native String getResult(int score);
     static {
        System.loadLibrary("scorechecker");
     }
}