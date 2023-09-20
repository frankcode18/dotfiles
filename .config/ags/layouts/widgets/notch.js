const { Button } = ags.Widget;
const { App } = ags;

export const Notch = props => Button({
    ...props,
    className: 'notch',
    onClicked: () => App.toggleWindow('dashboard'),
    connections: [[App, (btn, win, visible) => {
      btn.toggleClassName('active', win === 'dashboard' && visible);
  }]],
});