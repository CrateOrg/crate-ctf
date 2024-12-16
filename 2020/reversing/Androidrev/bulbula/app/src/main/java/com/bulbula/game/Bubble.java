package com.bulbula.game;

import android.animation.Animator;
import android.animation.ValueAnimator;
import android.content.Context;
import android.view.MotionEvent;
import android.view.ViewGroup;
import android.view.animation.LinearInterpolator;

import com.bulbula.game.utils.PixelHelper;

/**
 * Created by suhaas on 19/1/19.
 */

public class Bubble extends android.support.v7.widget.AppCompatImageView implements Animator.AnimatorListener, ValueAnimator.AnimatorUpdateListener {

    private ValueAnimator mAnimator;
    private BubbleListener mListener;
    private boolean mPopped;

    public Bubble(Context context) {
        super(context);
    }

    public Bubble(Context context, int color, int rawHeight) {
        super(context);

        mListener = (BubbleListener) context;


        this.setImageResource(R.mipmap.ic_soap_bubble_foreground);
//        this.setColorFilter(color);
//        this.setColorFilter(ContextCompat.getColor(context, R.color.colorBrightYarrow),
//                android.graphics.PorterDuff.Mode.MULTIPLY);

        int rawWidth = rawHeight / 2;

        int dpHeight = PixelHelper.pixelsToDp(rawHeight, context);
        int dpWidth = PixelHelper.pixelsToDp(rawWidth, context);

        ViewGroup.LayoutParams params = new ViewGroup.LayoutParams(dpWidth, dpHeight);
        this.setLayoutParams(params);

    }

    public void releaseBubble(int screenHeight, int duration) {

        mAnimator = new ValueAnimator();
        mAnimator.setDuration(duration);
        mAnimator.setFloatValues(screenHeight, 0f);
        mAnimator.setInterpolator(new LinearInterpolator());
        mAnimator.setTarget(this);
        mAnimator.addListener(this);
        mAnimator.addUpdateListener(this);
        mAnimator.start();
    }

    @Override
    public void onAnimationStart(Animator animator) {

    }

    @Override
    public void onAnimationEnd(Animator animator) {
        if (!mPopped) {
            mListener.popBubble(this, false);
        }
    }

    @Override
    public void onAnimationCancel(Animator animator) {
        if (!mPopped) {
            mListener.popBubble(this, false);
        }
    }

    @Override
    public void onAnimationRepeat(Animator animator) {

    }

    @Override
    public void onAnimationUpdate(ValueAnimator valueAnimator) {
        setY((Float) valueAnimator.getAnimatedValue());
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        if (!mPopped && event.getAction() == MotionEvent.ACTION_DOWN) {
            mListener.popBubble(this, true);
            mPopped = true;
            mAnimator.cancel();
        }

//        return super.onTouchEvent(event);
        return true;
    }

    public void setPopped(boolean popped) {
        mPopped = popped;
        if (popped) {
            mAnimator.cancel();
        }
    }

    public interface BubbleListener {
        void popBubble(Bubble bubble, boolean userTouch);
    }
}
