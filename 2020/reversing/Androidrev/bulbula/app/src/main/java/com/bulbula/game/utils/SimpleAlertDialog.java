package com.bulbula.game.utils;


import android.app.Dialog;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.DialogFragment;
import android.support.v7.app.AlertDialog;


public class SimpleAlertDialog extends DialogFragment {

    private static final String TITLE_KEY = "title_key";
    private static final String MESSAGE_KEY = "message_key";

    public SimpleAlertDialog() {
    }

    public static SimpleAlertDialog newInstance(String title, String message) {

        Bundle args = new Bundle();
        args.putString(TITLE_KEY, title);
        args.putString(MESSAGE_KEY, message);

        SimpleAlertDialog fragment = new SimpleAlertDialog();
        fragment.setArguments(args);
        return fragment;
    }

    @NonNull
    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {

        Bundle args = getArguments();
        if (args == null) throw new AssertionError();

        String title = args.getString(TITLE_KEY);
        String prompt = args.getString(MESSAGE_KEY);

        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity())
                .setTitle(title)
                .setMessage(prompt)
                .setCancelable(false);

        builder.setPositiveButton(android.R.string.ok, null);
        return builder.create();

    }

}