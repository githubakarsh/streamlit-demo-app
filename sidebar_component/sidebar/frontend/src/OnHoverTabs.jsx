import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";
import React from "react";
import { style } from 'glamor';
import "./component.css";
import "./icons/icon.css";

class OnHoverTabs extends StreamlitComponentBase {
  /**
   * Expects props.args.menuData to be an array of:
   * [
   *   {
   *     label: "Parent 1",
   *     icon: "home",
   *     children: [
   *       { label: "Child 1", icon: "star" },
   *       { label: "Child 2", icon: "settings" }
   *     ]
   *   },
   *   ...
   * ]
   */
  constructor(props) {
    super(props);
    this.state = {
      selectedParent: null,
      selectedChild: null,
    };
  }

  handleParentClick = (parent) => {
    this.setState(
      { selectedParent: parent, selectedChild: null },
      () => Streamlit.setComponentValue(parent.label)
    );
  };

  handleChildClick = (parent, child) => {
    this.setState(
      { selectedParent: parent, selectedChild: child },
      () => Streamlit.setComponentValue(child.label)
    );
  };
  render = () => {
    const labelName = this.props.args["tabName"];
    const iconName = this.props.args["iconName"];
    const styles = this.props.args['styles'] || {};

    let data = [];
    iconName.forEach((v, i) => (
      data = [...data, { id: i + 1, label: labelName[i], icon: v }]
    ));

    this.state = { icon: data[0].icon, label: data[0].label };

    const results = data.map(({ id, icon, label }) => (
      <span className="tab-container" {...style(styles['tabOptionsStyle'])} key={`wrap-${id}`}>
        <li
          className="tab"
          {...style(styles['tabStyle'])}
          onClick={() =>
            this.setState(
              () => ({ icon: icon, label: label }),
              () => Streamlit.setComponentValue(label)
            )
          }
        >
          <i className="material-icons" {...style(styles['iconStyle'])}>{icon}</i>
          <span className="labelName">{label}</span>
        </li>
      </span>
    ));

    return (
      <div className="navtab" {...style(styles['navtab'])}>
        <ul className="all-tabs-options">{results}</ul>
      </div>
    );
  };
}

export default withStreamlitConnection(OnHoverTabs);
